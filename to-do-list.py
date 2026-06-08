import tkinter as tk

root=tk.Tk()
root.geometry("800x500")
root.title("To Do List")

def add_command():
    task=ent.get()
    lbox.insert(tk.END,task)
    ent.delete(0,tk.END)

def mark_command():
    pos=lbox.curselection()[0]
    text=lbox.get(pos)
    lbox.delete(pos)
    lbox.insert(tk.END, f"{text} \u2713")

def del_command():
    pos=lbox.curselection()[0]
    lbox.delete(pos)

lbl=tk.Label(root,text="Enter Task:", font=('calibri',20))
lbl.place(x=20, y=20)

ent=tk.Entry(root,width=100)
ent.place(x=170 ,y=30)

lbox=tk.Listbox(root,width=100, height=20)
lbox.place(x=100 , y=70)

btn1=tk.Button(root,text="ADD", font=('calibri', 20), width=10,command=add_command)
btn1.place(x=75, y=420)

btn2=tk.Button(root,text="Mark", font=('calibri', 20), width=10, command=mark_command)
btn2.place(x=320, y=420)

btn3=tk.Button(root,text="Remove", font=('calibri', 20), width=10 ,command=del_command)
btn3.place(x=570, y=420)

root.mainloop()
