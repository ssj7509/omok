from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.simpledialog import*

class tkmain:
    test="abc"
    def __init__(self):
        self.widgets={}
        self.win=None

    def setWindow(self):
        self.win=Tk()
        self.win.title("tk_test")
        self.win.geometry("500x500+100+100")
        #self.setTopLevel()
        self.widgets["deltLbutton"]=Button(self.win,text="del",command=lambda:self.widgets["testtop"].destroy())
        self.widgets["deltLbutton"].pack()
        self.widgets["tstringvar"]=StringVar(self.win,"ttext")
        self.widgets["tEntry"]=Entry(self.win,textvariable=self.widgets["tstringvar"])
        self.widgets["tEntry"].pack()
        self.widgets["tButton"]=Button(self.win,text="tButton",command=self.tButton)
        self.widgets["tButton"].pack()
        self.widgets["tButton2"]=Button(self.win,text="tButton2",command=self.tButton2)
        self.widgets["tButton2"].pack()

        self.widgets["tCombobox"]=Combobox(self.win,values=[1,2,3])
        self.widgets["tCombobox"].pack()

        print(self.widgets["tCombobox"].current())

        
    def setTopLevel(self):
        topL=self.widgets["testtop"]=Toplevel(self.win)
        topL.geometry("300x300+150+150")
        topL.title("toplevel")
        topL.lift(aboveThis=self.win)

    def tButton(self):
        self.widgets["tEntry"].delete(0,END)

    def tButton2(self):
        print(self.widgets["tCombobox"].current())
    
    def run(self):
        self.setWindow()
        self.win.mainloop()

t=tkmain()
t.run()
