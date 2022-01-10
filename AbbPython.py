import sqlite3
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from functools import partial  
import csv


#connection to my local Database
conn = sqlite3.connect('WaferProbeMachine.db')
print("Database created and Successfully Connected to SQLite")
cur = conn.cursor()

"""
# used to test query
datumm = '2021.'
tabb = 717
eventt = 'CONTROL ERROR (POLLING)'
cur.execute("SELECT * FROM LogFile" + str(tabb) + " WHERE (Datum LIKE '%" + str(datumm) + "%' AND Event LIKE '%" + str(eventt) + "%') OR (Datum LIKE '%" + str(datumm) + "%' AND Event LIKE '%LOT-S,Lot start,,%')")
rows = cur.fetchall()

"""
# Create my GUI window
window = tk.Tk()
window.title ("ProbeMachine")
window.geometry("850x750")

#Labels 
#-------------------------------------------------
tab = tk.Label(window, text="Machine")
tab.grid(column=1, row=0)

startDat = tk.Label(window, text= "From")
startDat.grid(column=2, row=0)

endDat = tk.Label(window, text= "To")
endDat.grid(column=3, row=0)

event = tk.Label(window, text="Event")
event.grid(column=4, row=0)
#-------------------------------------------------


#Entries
#-------------------------------------------------

#Create a drop down menu for the machines
menu = StringVar()
menu.set("Select machine")
drop = tk.OptionMenu(window, menu,"715", "717","718","719","720","723")
drop.grid(column=1, row=1)

#datumInput = tk.Entry(window,width=20)
#datumInput.grid(column=2, row=1)

startDateInput = tk.Entry(window,width=20)
startDateInput.grid(column=2, row=1)

endDateInput = tk.Entry(window,width=20)
endDateInput.grid(column=3, row=1)


eventInput = tk.Entry(window,width=50)
eventInput.grid(column=4, row=1)
#--------------------------------------------------


# Text areas
#-------------------------------------------------
text_area = tk.scrolledtext.ScrolledText(window, width = 100, height = 35)
text_area.grid(column = 1, columnspan=5, row=3, pady = 10, padx = 10, )

text_area1 = tk.scrolledtext.ScrolledText(window, width = 100, height = 1)
text_area1.grid(column = 1, columnspan=5, row=4, pady = 10, padx = 10)



#Button Functions 
#---------------------------------------------------
"""
def clickedRead():
    datumm = datumInput.get()
    tabb = menu.get()
    #tabb = tabInput.get()
    eventt = eventInput.get()
    
    cur.execute("SELECT * FROM LogFile" + str(tabb) + " WHERE (Datum LIKE '%" + str(datumm) + "%' AND Event LIKE '%" + str(eventt) + "%') OR (Datum LIKE '%" + str(datumm) + "%' AND Event LIKE '%LOT-S,Lot start,,%')")
    rows = cur.fetchall()
    text_area.delete(1.0, END)
    text_area1.delete(1.0, END)
    count = 0
    #for i in range (len(rows)):
    #    text_area.insert(tk.INSERT, (rows [i], "\n"))   

    
    for i in range (len(rows)):
        for sub in rows [i]:
            if str(sub).__contains__('ERROR'):
                text_area.insert(tk.INSERT, (rows [i-1], "\n"))
                text_area.insert(tk.INSERT, (rows [i], "\n"))
                count = count + 1
    text_area1.insert(tk.INSERT, ("This event shows up ", count, " times"))  
"""


def clickedRead():
    startDate = startDateInput.get()
    endDate = endDateInput.get()
    tabb = menu.get()
    #tabb = tabInput.get()
    eventt = eventInput.get()
    
    cur.execute("SELECT * FROM LogFile" + str(tabb) + " WHERE ((Datum BETWEEN '"+ str(startDate)+"' AND '"+ str(endDate)+"') AND Event LIKE '%" + str(eventt) + "%') OR ((Datum BETWEEN '"+ str(startDate)+"' AND '"+ str(endDate)+"') AND Event LIKE '%LOT-S,Lot start,,%')")
    #cur.execute("SELECT * FROM LogFile" + str(tabb) + " WHERE ((Datum BETWEEN '"+ str(startDate)+"' AND '"+ str(endDate)+"') AND Event LIKE '%" + str(eventt) + "%') OR ((Datum BETWEEN '"+ str(startDate)+"' AND '"+ str(endDate)+"'))")
    #cur.execute("SELECT * FROM LogFile" + str(tabb) + " WHERE ((Datum BETWEEN '"+ str(startDate)+"' AND '"+ str(endDate)+"') AND Event LIKE '%" + str(eventt) + "%') OR ((Datum BETWEEN '"+ str(startDate)+"' AND '"+ str(endDate)+"') AND Event LIKE '%LOT-E,Lot done,%')")
    

    rows = cur.fetchall()
    text_area.delete(1.0, END)
    text_area1.delete(1.0, END)
    count = 0
    #for i in range (len(rows)):
    #    text_area.insert(tk.INSERT, (rows [i], "\n"))   

    
    for i in range (len(rows)):
        for sub in rows [i]:
            if str(sub).__contains__(str(eventt)):
            #if str(sub).__contains__('ERROR'):
                text_area.insert(tk.INSERT, (rows [i-1], "\n"))
                text_area.insert(tk.INSERT, (rows [i], "\n"))
                #text_area.insert(tk.INSERT, (rows [i+1], "\n"))
                count = count + 1
    text_area1.insert(tk.INSERT, ("This event shows up ", count, " times"))           
#--------------------------------------------------------

def clickedCSV():
    startDate = startDateInput.get()
    endDate = endDateInput.get()
    tabb = menu.get()
    #tabb = tabInput.get()
    eventt = eventInput.get()
    mylist = []
    cur.execute("SELECT * FROM LogFile" + str(tabb) + " WHERE ((Datum BETWEEN '"+ str(startDate)+"' AND '"+ str(endDate)+"') AND Event LIKE '%" + str(eventt) + "%') OR ((Datum BETWEEN '"+ str(startDate)+"' AND '"+ str(endDate)+"') AND Event LIKE '%LOT-S,Lot start,,%')")
    rows = cur.fetchall()
    count = 0
    #for i in range (len(rows)):
    #    text_area.insert(tk.INSERT, (rows [i], "\n"))   

    
    for i in range (len(rows)):
        for sub in rows [i]:
            if str(sub).__contains__('ERROR'):
                mylist.append(rows [i-1])
                mylist.append(rows [i])

    with open('myfile.csv', 'w', newline='') as myfile:
        for row in mylist:
            wr = csv.writer(myfile)
            #wr.__delattr__: ";"
            wr.writerow(row)


#Buttons
#---------------------------------------------------------------
btnRead = tk.Button(window, width =15, text="Read", command=clickedRead)
btnRead.grid(column=5, row=1, sticky="ew")

btnCSV = tk.Button(window, width =15, text="CSV", command=clickedCSV)
btnCSV.grid(column=1, row=5, sticky="ew", pady = 10, padx = 10)
#---------------------------------------------------------------

window.mainloop()
