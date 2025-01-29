import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image

log= tk.Tk()
log.geometry("600x300")
log.title("Login")
background_image = ImageTk.PhotoImage(file="logbg.jpg")
background_label = tk.Label(log,image=background_image)
background_label.place(x=0, y=0)

loghead = tk.Label(log, text = "LOGIN")
loghead.config(font=("Courier", 44))
loghead.place(x =220 , y = 10)
  
username=tk.Label(log,text="Enter Username",width=20,font=("bold", 10))
username.config(font=("Courier", 10))
username.place(x=80,y=130)

inputusername = tk.Entry(log)  
inputusername.place(x=300,y=130)  

password=tk.Label(log,text="Enter Password",width=20,font=("bold", 10))
password.config(font=("Courier", 10))
password.place(x=80,y=180)  

inputpassword = tk.Entry(log,show="*")  
inputpassword.place(x=300,y=180)  

tk.Button(log, text='Submit',width=20,bd= 0,bg='#2271F4',fg='white',).place(x=250,y=220) 
#def login_successful():
 #   messagebox.showinfo(title="login", message="Login Successful")   
log.mainloop()

