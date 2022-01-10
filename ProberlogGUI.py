import ftplib
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from functools import partial  
import csv
from io import BytesIO

FTP_HOST = '----------'
FTP_USER = '----------'
FTP_PASS = '---------'
#--------------------------------------------------------------------------------

# Create my GUI window
window = tk.Tk()
window.title ("ProbeMachine")
window.geometry("850x750")

#Labels 
#-------------------------------------------------
startDat = tk.Label(window, text= "From")
startDat.grid(column=2, row=0)

"""
menu = StringVar()
menu.set("Select machine")
drop = tk.OptionMenu(window, menu,"715", "717","718","719","720","723")
drop.grid(column=1, row=1)
"""



#Entries
#-------------------------------------------------
drop = tk.Entry(window,width=20)
drop.grid(column=1, row=1)

startDateInput = tk.Entry(window,width=20)
startDateInput.grid(column=2, row=1)

endDateInput = tk.Entry(window,width=20)
endDateInput.grid(column=3, row=1)

eventInput = tk.Entry(window, width = 20)
eventInput.grid(column=4, row = 1)



# Text areas
#-------------------------------------------------
text_area = tk.scrolledtext.ScrolledText(window, width = 100, height = 35)
text_area.grid(column = 1, columnspan=5, row=3, pady = 10, padx = 10, )




#---------------------------------------------------
def clickedRead():
    # connect to the FTP server
    ftp = ftplib.FTP(FTP_HOST, FTP_USER, FTP_PASS)
    # force UTF-8 encoding
    ftp.encoding = "utf-8"
    dropS = drop.get()
    print(dropS)
    ftp.cwd('/QR-FTP/log/QR'+ dropS + '/')
    
    filename = startDateInput.get()+".log"

    
    #filename = startDateInput +".log"
    #ftp.dir()
    with open(filename, "wb") as f:
        text_area.delete(1.0, END)
        r = BytesIO()
        ftp.retrbinary('RETR ' + filename, r.write)
        test = r.getvalue()
        #input = startDateInputs[0:4] + "." + startDateInputs[4:6] + "." + startDateInputs[6:8]
        input = filename[0:4] + "." + filename[4:6] + "." + filename[6:8]
        print(input)
        arr = str(test).split(input)
        arr1 = []
        for x in arr:
            print(x)
            if eventInput.get() in x:
                #text_area.insert(tk.INSERT, (x, "\n"))
                text_area.insert(tk.INSERT, (x, "\n"))


#clickedRead()

#ftp.quit()
   # endDate = endDateInput.get()
    #tabb = menu.get()
    #tabb = tabInput.get()
    #eventt = eventInput.get()
    #
    #text_area1.delete(1.0, END)
    
    #for i in range (len(rows)):
    #    text_area.insert(tk.INSERT, (rows [i], "\n"))   
    
"""
        for sub in rows [i]:
            if str(sub).__contains__(str(eventt)):
            #if str(sub).__contains__('ERROR'):
                text_area.insert(tk.INSERT, (rows [i-1], "\n"))
                text_area.insert(tk.INSERT, (rows [i], "\n"))
                count = count + 1
    text_area1.insert(tk.INSERT, ("This event shows up ", count, " times"))   
"""        
#--------------------------------------------------------
#Buttons
#---------------------------------------------------------------
btnRead = tk.Button(window, width =15, text="Read", command=clickedRead)
btnRead.grid(column=5, row=1, sticky="ew")
#---------------------------------------------------------------
window.mainloop()
