#!/usr/bin/env python
# coding: utf-8

# In[1]:


import onetimepad


# In[2]:


from tkinter import *
#import tkinter

win = Tk()
win.title("Chryptography App")

def encryptMessage():
    a = var.get()
    
    ct = onetimepad.encrypt(a,"random")
    print("Working",ct) 
    
    e2.delete(0,END)
    e2.insert(END,ct)

def dycrptMessage():
    a = var2.get()

    ct = onetimepad.decrypt(a,"random")
    print("Working",ct) 
    
    e4.delete(0,END)
    e4.insert(END,ct)
    
    
    
l1 = Label(win,text="Plain Text")
l1.grid(row=0,column=0)


l3 = Label(win,text="Encypted Text")
l3.grid(row=0,column=2)

var= StringVar()
e1 = Entry(win,textvariable=var)
e1.grid(row=0,column=1)

var2= StringVar()
e3 = Entry(win,textvariable=var2)
e3.grid(row=0,column=3)



l2 = Label(win,text="Encypted Text")
l2.grid(row=1,column=0)

l4 = Label(win,text="Plain Text")
l4.grid(row=1,column=2)


e2 = Entry(win)
e2.grid(row=1,column=1)

e4 = Entry(win)
e4.grid(row=1,column=3)

b1 = Button(win,text="Encyption",bg="blue",fg="Red",command=encryptMessage)
b1.grid(row=2,column=1)

b2 = Button(win,text="Dycrption",bg="blue",fg="Red",command=dycrptMessage)
b2.grid(row=2,column=3)




root.mainloop()


# In[ ]:




