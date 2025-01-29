import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter.filedialog import askopenfile
#window
startpage=tk.Tk()
startpage.geometry("800x480") 
startpage.title("Home Page")
background_image = ImageTk.PhotoImage(file='bg.jpg')

#login window
def login_win():
   log= tk.Toplevel(startpage)
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

   tk.Button(log, text='Submit',width=20,bd= 0,bg='#2271F4',fg='white',command=login_successful,).place(x=250,y=220) 
   
   log.mainloop()

def login_successful():
    messagebox.showinfo(title="login", message="Login Successful")

def signup_successful():
    messagebox.showinfo(title="login", message="Signup Successful")


#signup window
def signup_win():
   signup= tk.Toplevel(startpage)
   signup.geometry("750x600")
   signup.title("SignUp")
   background_sign = ImageTk.PhotoImage(file="bgsign.jpg")
   background_label = tk.Label(signup,image=background_sign)
   background_label.place(x=0, y=0)

   signhead = tk.Label(signup, text = "SIGN UP")
   signhead.config(font=("Courier", 44))
   signhead.place(x =270 , y = 10)

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
   
   uploadpic=tk.Label(signup, text="Upload Photo:",width=20)
   uploadpic.config(font=("Courier", 12))
   uploadpic.place(x=180,y=410)
# upload image
   b1 = tk.Button(signup, text='Upload File', width=20,command = lambda:upload_file())
   b1.place(x=400,y=410) 
   
   def upload_file():
    global img
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img=Image.open(filename)
    img_resized=img.resize((75,100)) # new width & height
    img=ImageTk.PhotoImage(img_resized)
    b2 =tk.Button(signup,image=img) # using Button 
    b2.place(x=600,y=350)
    
   tk.Button(signup, text='Submit',width=20,bd= 0,bg='#2271F4',fg='white',command=signup_successful).place(x=300,y=500) 
   signup.mainloop()

#background
bglabel = tk.Label(startpage, image=background_image)
bglabel.place(x=0,y=0)



#welcome line
welcome = tk.Label(startpage, text = "WELCOME")
welcome.config(font=("Courier", 44))
welcome.place(x =275 , y = 75)

#intro line
intro = tk.Label(startpage, text = "You've stepped into world of endless opportunities!")
intro.config(font=("Courier", 15 ))
intro.place(x = 100, y = 200)

#login button
log = tk.Button(startpage, text ="Login",  bg='#146BC1',fg='#ffffff',bd=0,height=2,width=15, command=login_win)
log.place(x=250,y=300)

#signin button
sign = tk.Button(startpage, text ="Sign Up", bg='#146BC1',fg='#ffffff',bd=0,height=2,width=15, command=signup_win)
sign.place(x=400,y=300)


startpage.mainloop()
