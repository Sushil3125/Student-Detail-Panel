from test import start
from tkinter import *
from numpy import heaviside
import pandas as pd
from pandastable import Table, TableModel
import time

from pandas.core.indexes.base import Index

primary_database=pd.DataFrame()

class myWindow:
    def __init__(self, win):
        self.lab1=Label(win, text="Enter Student Details Below",font=('Helvetica',20))
        self.id_lab=Label(win, text="ID")
        self.first_lab=Label(win, text="First Name")
        self.last_lab=Label(win, text="Last Name")
        self.email_lab=Label(win, text="Email")
        self.grade_lab=Label(win, text="Grade")

        self.submit_but=Button(win, text="Submit" , command= lambda: self.submit(win, primary_database))
        self.save=Button(win, text="Display Database" , command= lambda: self.display_data(win, ))

        self.id_e=Entry(bd=3)
        self.fi_e=Entry(bd=3)
        self.la_e=Entry(bd=3)
        self.em_e=Entry(bd=3)
        self.gr_e=Entry(bd=3)

        self.lab1.place(x=0, y=10)
        self.id_lab.place(x=25, y=75)
        self.first_lab.place(x=25, y=105)
        self.last_lab.place(x=25, y=135)
        self.email_lab.place(x=25, y=165)
        self.grade_lab.place(x=25, y=195)
        self.id_e.place(x=100,y=75)
        self.fi_e.place(x=100,y=105)
        self.la_e.place(x=100,y=135)
        self.em_e.place(x=100,y=165)
        self.gr_e.place(x=100,y=195)

        self.submit_but.place(x=200, y=225)
        self.save.place(x=300, y=225)

    def killWin(self):
        killWindow()
    
    def clearWig(self):
        clear_frame()


    def submit(self, win, primary_database):
        print('Submtted')
        detail_dic={
            'id': self.id_e.get(),
            'first': self.fi_e.get(),
            'last': self.la_e.get(), 
            'email': self.em_e.get(),
            'grade': self.gr_e.get(),
        }
        print(detail_dic)
        primary_database = primary_database.append(detail_dic, ignore_index=True)
        primary_database=primary_database.set_index('id')
        print(primary_database)
        self.id_e.delete(0, 'end')
        self.fi_e.delete(0, 'end')
        self.la_e.delete(0, 'end')
        self.em_e.delete(0, 'end')
        self.gr_e.delete(0, 'end')


    # def save_to_sec(self, win, primary_database):
        primary_database.to_csv('Primary Datavase.csv', mode='a', header=False)
        print('File Saved')

    def display_data(self, parent=None):
        start()



if __name__=="__main__":
    windows =Tk()
    myWin=myWindow(windows)
    windows.title("Student Details Panel")
    windows.geometry('540x360')
    def killWindow():
        windows.destroy()
    def clear_frame():
        for widgets in windows.winfo_children():
            widgets.destroy()
    windows.mainloop()