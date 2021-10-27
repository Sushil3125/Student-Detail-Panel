from numpy import flatiter, true_divide
from tkinter import *
from tkinter import messagebox
import pandas as pd
import time
import csv
from pandas.core.indexes.base import Index
from pandas.core.window.rolling import Window


try: 
    df=pd.read_csv("Primary Database.csv")
    
except:
    df=pd.DataFrame(columns=["id", "first", "last", "email", "grade"])



class myWindow:
    def __init__(self, win):
        self.lab1=Label(win, text="Enter Student Details Below",font=('Helvetica',20))
        self.id_lab=Label(win, text="ID")
        self.first_lab=Label(win, text="First Name")
        self.last_lab=Label(win, text="Last Name")
        self.email_lab=Label(win, text="Email")
        self.grade_lab=Label(win, text="Grade")

        self.submit_but=Button(win, text="Submit" , command= lambda: self.submit(win, df))
        self.save=Button(win, text="Display Database" , command= lambda: self.display_data(win))
        self.delete_but=Button(win, text="Delete/ Edit", command= lambda : self.delete(win, df))
        self.save_but=Button(win, text="Save to Database", command= lambda : self.save_to_db(win, df))


        self.id_e=Entry(bd=3)
        self.fi_e=Entry(bd=3)
        self.la_e=Entry(bd=3)
        self.em_e=Entry(bd=3)
        self.gr_e=Entry(bd=3)
        
        self.text_box=Text(height=20, width=55)
        

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

        self.submit_but.place(x=75, y=235)
        self.save.place(x=175, y=235)
        self.delete_but.place(x=75, y= 285)
        self.save_but.place(x=175, y= 285)

        self.text_box.place(x=300, y=75)


    def killWin(self):
        killWindow()
    
    def clearWig(self):
        clear_frame()


    def submit(self, win, df):
        detail_dic={
            'id': self.id_e.get(),
            'first': self.fi_e.get(),
            'last': self.la_e.get(), 
            'email': self.em_e.get(),
            'grade': self.gr_e.get(),
        }
        print('Submtted')
        print(detail_dic)
        # df=df.append(detail_dic, ignore_index=True, sort=False)
        df.loc[len(df.index)] = detail_dic
        print("Done")
        messagebox.showinfo("Message","Submitted Succesfully")
        self.id_e.delete(0, 'end')
        self.fi_e.delete(0, 'end')
        self.la_e.delete(0, 'end')
        self.em_e.delete(0, 'end')
        self.gr_e.delete(0, 'end')

        self.display_data(win)
        # primary_database.to_csv('Primary Datavase.csv', mode='a', header=False)
        # print('File Saved')
    def delete(self, win, primary_database):
        self.delete_txt=Label(win, text="Enter ID of student the student detail.")
        self.delete_txt.place(x=25,y=310)
        self.delete_id=Entry(bd=3)
        self.delete_id.place(x=25,y=350)
        self.del_ele=Button(win, text="Delete Element", command= lambda : self.Del_ele_fun(win, df))
        self.del_ele.place(x=200, y=350)
        self.del_ele=Button(win, text="Edit Element", command= lambda : self.edit_ele_fun(win, df))
        self.del_ele.place(x=200, y=400)
        return
    
    def save_to_db(self,win, df):
           # primary_database.to_csv('Primary Datavase.csv', mode='a', header=False)
        # print('File Saved')
        df.to_csv('Primary Database.csv', index=False)
        messagebox.showinfo("Message","Data Saved")
        print('File Saved')
        
    def edit_ele_fun(self, win, df):
        id=int(self.delete_id.get())
        count=0
        for x in df['id']:
            if int(x)==id:
                break
            else:
                count+=1
        print(count)
        a_dict=df.iloc[count]
        print(a_dict)
        self.id_e.insert(0,a_dict['id'])
        self.fi_e.insert(0,a_dict['first'])
        self.la_e.insert(0,a_dict['last'])
        self.em_e.insert(0,a_dict['email'])
        self.gr_e.insert(0,a_dict['grade'])
        df.drop(df.index[count], inplace=True)         
        self.delete_id.delete(0, 'end')

    def Del_ele_fun(self, win, df):
        id=self.delete_id.get()
        id=int(id)
        count=0
        for x in df['id']:
            if int(x)==id:
                break
            else:
                count+=1
        print(count)
        df.drop(df.index[count], inplace=True) 
        messagebox.showinfo("Message","Deleted Succesfully")
        print('Done')  
        self.delete_id.delete(0, 'end')

    def display_data(self, win):
        self.text_box.delete("0.0", END)
        self.text_box.insert("0.0",df)

        



if __name__=="__main__":
    count=0
    windows =Tk()
    myWin=myWindow(windows)
    windows.title("Student Details Panel")
    windows.geometry('775x450')
    def killWindow():
        windows.destroy()
    def clear_frame():
        for widgets in windows.winfo_children():
            widgets.destroy()
    windows.mainloop()

