import ftplib
from tkinter import *
import tkinter as tk
from tkinter import scrolledtext
from functools import partial  
from typing import Counter
import os
#----------------------------------------------------------------------------------------------------------------------------------------------
date = []
year = 2017
for y in range (1, 11):
    year += 1
    month =0
    for m in range (1, 13):
        month += 1
        day = 0
        for d in range (1, 32):
            day += 1
            if ((day == 1 or day == 2 or day == 3 or day == 4 or day == 5 or day == 6 or day == 7 or day == 8 or day == 9) and 
            (month == 1 or month == 2 or month == 3 or month == 4 or month == 5 or month == 6 or month == 7 or month == 8 or month == 9)):
                date.append(str(year) + '0' + str(month) + '0' + str(day))
            elif ((day == 1 or day == 2 or day == 3 or day == 4 or day == 5 or day == 6 or day == 7 or day == 8 or day == 9) and 
            (month != 1 or month != 2 or month != 3 or month != 4 or month != 5 or month != 6 or month != 7 or month != 8 or month != 9)):
                date.append(str(year) + str(month) + '0' + str(day))
            elif ((day != 1 or day != 2 or day != 3 or day != 4 or day != 5 or day != 6 or day != 7 or day != 8 or day != 9) and 
            (month == 1 or month == 2 or month == 3 or month == 4 or month == 5 or month == 6 or month == 7 or month == 8 or month == 9)):
                date.append(str(year) + '0' + str(month) + str(day))
            else: 
                date.append(str(year) + str(month) + str(day))

for x in date:
    if str(x).__contains__('0229'):
        date.remove(x)
for x in date:   
    if str(x).__contains__('0230'):
        date.remove(x)
for x in date:   
    if str(x).__contains__('0231'):
        date.remove(x)

for x in date:
    if str(x).__contains__('0431'):
        date.remove(x)

for x in date:
    if str(x).__contains__('0631'):
        date.remove(x)
for x in date:
    if str(x).__contains__('0931'):
        date.remove(x)                
for x in date:
    if str(x).__contains__('1131'):
        date.remove(x)

#----------------------------------------------------------------------------------------------------------------------------------------------------

# Create my GUI window-------------------------------------------
window = tk.Tk()
window.title ("ProbeMachine")
window.geometry("850x750")

#Labels----------------------------------------------------------
tab = tk.Label(window, text="Machine")
tab.grid(column=1, row=0)

startDat = tk.Label(window, text= "From")
startDat.grid(column=2, row=0)

endDat = tk.Label(window, text= "To")
endDat.grid(column=3, row=0)

event = tk.Label(window, text="Event")
event.grid(column=4, row=0)

#Entries---------------------------------------------------------
menu = StringVar()
menu.set("Select machine")
drop = tk.OptionMenu(window, menu,"715", "717","718","719","722","723")
drop.grid(column=1, row=1)

menuStartDay = StringVar()
menuStartDay.set("day")
drop = tk.OptionMenu(window, menuStartDay,"01", "02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
drop.grid(column=2, row=1)

menuStartMonth = StringVar()
menuStartMonth.set("Month")
drop = tk.OptionMenu(window, menuStartMonth,"01", "02","03","04","05","06","07","08","09","10","11","12")
drop.grid(column=2, row=2)

menuStartYear = StringVar()
menuStartYear.set("Year")
drop = tk.OptionMenu(window, menuStartYear,"2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027")
drop.grid(column=2, row=3)

menuEndDay = StringVar()
menuEndDay.set("day")
drop = tk.OptionMenu(window, menuEndDay,"01", "02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31")
drop.grid(column=3, row=1)

menuEndMonth = StringVar()
menuEndMonth.set("Month")
drop = tk.OptionMenu(window, menuEndMonth,"01", "02","03","04","05","06","07","08","09","10","11","12")
drop.grid(column=3, row=2)

menuEndYear = StringVar()
menuEndYear.set("Year")
drop = tk.OptionMenu(window, menuEndYear,"2017","2018","2019","2020","2021","2022","2023","2024","2025","2026","2027")
drop.grid(column=3, row=3)

eventInput = tk.Entry(window,width=50)
eventInput.grid(column=4, row=1)

#Button Functions------------------------------------------------
def clickedRead():
    Alllines = []
    Alllines2 = []
    counter = 0
    machineMenu = str(menu.get())
    startDate = menuStartYear.get()+ menuStartMonth.get()+menuStartDay.get() 
    endDate = menuEndYear.get()+ menuEndMonth.get()+menuEndDay.get()
    eventInputStr = str(eventInput.get())
   
    startDateInt = int(date.index(startDate))
    endDateInt = int(date.index(endDate))

#Download Files from FTP SERVER------------------------------------
    FTP_HOST = "---------"
    FTP_USER = "-------"
    FTP_PASS = "--------"
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)          # connect to the FTP server
    ftp.encoding = "utf-8"                                  # force UTF-8 encoding
#Where the magic happens--------------------------------------------
    for i in range (startDateInt, (endDateInt + 1)):
        filename = date[i] + ".log"
        #print(filename + '  holaaaa')
        with open(filename, "wb") as f:
            ftp.cwd('/QR-FTP/log/QR'+ machineMenu +'/')
            localfile = open(filename, 'wb')
            ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
            with open(filename) as f:
                for x in f:
                    Alllines.append(x)
    
    for y in Alllines:
        if str(y).__contains__(str(eventInputStr)) or str(y).__contains__('Lot start'):
            Alllines2.append(y)
                    
    for z in Alllines2:
        if str(z).__contains__(str(eventInputStr)):
            text_area.insert(tk.INSERT, (Alllines2[(Alllines2.index(z)-1)]))
            text_area.insert(tk.INSERT, z)             
            counter += 1                       
    ftp.quit()   
    text_area1.insert(tk.INSERT, counter)


def clickedClear():
    dir_list = os.listdir("C:\\Users\\charroc1\\Desktop\\LogFileFilter")
    for x in dir_list:
        if "log" in x:
            os.remove(x)

    text_area.delete(1.0, END)
    text_area1.delete(1.0, END)

# Text areas----------------------------------------------
text_area = tk.scrolledtext.ScrolledText(window, width = 100, height = 35)
text_area.grid(column = 1, columnspan=5, row=4, pady = 10, padx = 10, )

text_area1 = tk.scrolledtext.ScrolledText(window, width = 100, height = 1)
text_area1.grid(column = 1, columnspan=5, row=5, pady = 10, padx = 10)


#Buttons----------------------------------------------------------
btnRead = tk.Button(window, width =15, text="Read", command=clickedRead)
btnRead.grid(column=5, row=1, sticky="ew")

btnClear = tk.Button(window, width =15, text="Clear", command=clickedClear)
btnClear.grid(column=5, row=2, sticky="ew")

window.mainloop()