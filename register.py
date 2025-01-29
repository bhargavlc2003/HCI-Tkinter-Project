import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image

signup= tk.Tk()
signup.geometry("750x600")
signup.title("SignUp")

background_sign = ImageTk.PhotoImage(file="bgsign.jpg")

background_label = tk.Label(signup,image=background_sign)
background_label.place(x=0, y=0)

signhead = tk.Label(signup, text = "Student Register")
signhead.config(font=("Courier", 44))
signhead.place(x =130 , y = 10)

fullname=tk.Label(signup,text="Enter Full Name:",width=20)
fullname.config(font=("Courier", 12))
fullname.place(x=180,y=110)

ipname = tk.Entry(signup)  
ipname.place(x=400,y=110)

address=tk.Label(signup,text="Enter Address:",width=20)
address.config(font=("Courier", 12))
address.place(x=180,y=160)

ipaddr = tk.Entry(signup)  
ipaddr.place(x=400,y=160)

email=tk.Label(signup,text="Enter Email Address:",width=20)
email.config(font=("Courier", 12))
email.place(x=180,y=210)

ipemail = tk.Entry(signup)  
ipemail.place(x=400,y=210)

mobile=tk.Label(signup,text="Enter Mobile No:",width=20)
mobile.config(font=("Courier", 12))
mobile.place(x=180,y=260)

ipmobile = tk.Entry(signup)  
ipmobile.place(x=400,y=260)

city=tk.Label(signup,text="City & Pincode:",width=20)
city.config(font=("Courier", 12))
city.place(x=180,y=310)

ipcity = tk.Entry(signup)  
ipcity.place(x=400,y=310)

gender=tk.Label(signup, text="Gender:",width=20)
gender.config(font=("Courier", 12))
gender.place(x=180,y=360)

male_radio = tk.Radiobutton(signup, text="Male", value="Male")
male_radio.place(x=400,y=360)
female_radio = tk.Radiobutton(signup, text="Female", value="Female")
female_radio.place(x=460,y=360)


 
tk.Button(signup, text='Submit',width=20,bd= 0,bg='#2271F4',fg='white',).place(x=300,y=500) 
signup.mainloop()