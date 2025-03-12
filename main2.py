import tkinter as tk 
from math import sin , cos ,tan , log , sqrt, pi ,e ,radians,  degrees , asin , acos , atan 

in_degrees = True

def click (event):

    global in_degrees
    text = event.widget.cget("text")

    if text ==  "=" :
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except Exception as e :
            screen_var.set("Error")

    elif text == "C":
        screen_var.set("")

    elif text == "√":
        try:
            result = sqrt(eval(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
            
    elif text == "𝛑":
        screen_var.set(screen.get()+str(pi))

    elif text == "e":
        screen_var.set(screen.get()+str(e))

    elif text in [ "sin" , "cos" ,"ten" , "log","asin","acos","atan" ]:
        try:
            expression = eval( sereen.get())
            if in_degrees :
                expression = radians(expression)
            if text == "sin":
                result = sin(expression)
            elif text =="cos" :
                result= cos(expression)
            elif text == "tan":
                result = tan(expression)
            elif text == "asin":
                result = degrees(asin(expression))if in_degrees else asin(expression)
            elif text == "acos":
                result = degrees(acos(expression))if in_degrees else acos(expression)
            elif text == "atan":
                result = degrees(atan(expression))if in_degrees else atan(expression)
            screen_var.set(result)
        except Exception as e :
            screen_var.set("Error")

    elif text == "log":
        try:
            result = log(eval(screen.get))
            screen_var.set(result)
        except Exception as e :
            screen_var.set("Error")

    elif text == "deg":
        in_degrees = True 
        screen_var.set("degreea mode")

    elif text == "red":
        in_degrees = False
        screen_var.set("radiance mode")
    else:
        screen_var.set(screen.get()+ text)

root = tk.Tk()
# root.geometry("450x600")
root.geometry()
root.title("calculator")

screen_var =  tk.StringVar()
screen_var.set("")
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.pack(fill=tk.BOTH,ipadx=3, pady=5, padx=5)

frame = tk.Frame(root)
frame.pack()

buttons = [
    ['sin' , 'cos' ,'ten' , 'red', 'deg'  ],
    ['log' , 'In','(',')','inv'],
    ['!','C','%','√','/'],
    ['^','7','8','9','x'],
    ['𝛑','4','5','6','-'],
    ['e','1','2','3','+'],
    ['00','0','.','=',''],
]

for button_row in buttons:
    row = tk.Frame(frame)
    row.pack(side=tk.TOP,fill = tk.BOTH,expand=True)
    for button in button_row:
        if button != '':
            # b = tk.Button(row, text=button,font="lucida 15 bold",relief=tk.RAISED, bd=2, padx=20 , pady=20)
            b = tk.Button(row, text=button , )
            b.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
            b.bind("<Button-1>",click)

root.mainloop()