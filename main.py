import tkinter as tk

def add():
    result.set(float(num1.get())+float(num2.get()))
def subtract():
    result.set(float(num1.get())-float(num2.get()))
def multiply():
    result.set(float(num1.get())*float(num2.get()))
def divide():
    result.set(float(num1.get())/float(num2.get()))
def peersentile():
    result.set(float(num1.get())**float(num2.get()))

    

window = tk.Tk()
window.title("calculater")

num1 = tk.StringVar()
num2 = tk.StringVar()
result = tk.StringVar()

tk.Label(window,text="Number 1:").grid(row=0, column=0)
tk.Entry(window,textvariable=num1).grid(row=0, column=1)

tk.Label(window,text="Number 2:").grid(row=1, column=0)
tk.Entry(window,textvariable=num2).grid(row=1, column=1)

tk.Button(window, text= "+", command= add ).grid(row=2 , column=0)
tk.Button(window, text= "^", command= peersentile).grid(row=2 , column=1)
tk.Button(window, text= "-", command= subtract ).grid(row=2 , column=3)
tk.Button(window, text= "*", command=  multiply).grid(row=3 , column=0)
tk.Button(window, text= "/", command= divide ).grid(row=3 , column=3)
tk.Button(window, text="quit", command=quit ).grid(row=3 ,column=1)
tk.Button(window, text="clear",command=0 ).grid(row=4 ,column=3)


tk.Label(window,text="Result :").grid(row=0, column=3)
tk.Label(window,textvariable=result).grid(row=1, column=3)
window.mainloop()