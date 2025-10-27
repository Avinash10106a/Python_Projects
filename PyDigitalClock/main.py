# from tkinter import Tk,Label
# from time import strftime

# root=Tk()
# root.title("Digital_Clock")

# label = Label(root,font=("caliber",20,'bold'),background='black',foreground='white')

# def runtime():
#     string = strftime("%H:%M:%S \n %D")
#     label.config(text=string)
#     label.after(1000,runtime)
# label.pack(anchor='center')
# runtime()

# label.mainloop()


from tkinter import Tk,Label
from time import strftime as sft

root = Tk()

label=Label(root,font=("caliber",20,"bold"),background="Black",foreground="white")

def runtime():
    string = sft(f"%H:%M:%S \n %D")
    label.config(text=string)
    label.after(1000,runtime)

label.pack(anchor="center")
runtime()
label.mainloop()
