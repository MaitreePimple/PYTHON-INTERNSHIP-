import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(expression)
            display_var.set(result)
            expression =str(result)
        except Exception as e:
            display_var.set("Error")
            expression = ""
    elif text =="C":
        expression =""
        display_var.set("")
    else:
        expression += text
        display_var.set(expression)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
expression = ""

display_var = tk.StringVar()
display = tk.Entry(root, textvar=display_var, font="Arial 20 ", bg="lightgrey", justify="right")
display.pack(fill=tk.BOTH, ipadx=8, pady= 10, padx=20)
root.configure(bg ="#CBC3E3")
button_frame =tk.Frame(root, bg="black")
button_frame.pack()

buttons =[
    ['7','8','9','+'],
    ['4','5','6','-'],
    ['1','2','3','*'],
    ['C','0','=','/']
]

button_colors={"C": "red", "=": "green", "0": "lightblue", "+": "orange", "-": "orange", "*": "orange", "/": "orange"}

for row in buttons:
    frame_row =tk.Frame(button_frame) 
    frame_row.pack()
    for button_text in row:
        color=button_colors.get(button_text,"lightgray")
        button = tk.Button(frame_row, text=button_text,font="Arial 15 bold", bg=color, width=5, height=2)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()    
        

