import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk,Image

review= tk.Tk()
review.geometry("750x600")
review.title("review")

background_sign = ImageTk.PhotoImage(file="bgreview.jpg")

background_label = tk.Label(review,image=background_sign)
background_label.place(x=0, y=0)

signhead = tk.Label(review, text = "Food Review")
signhead.config(font=("Courier", 44))
signhead.place(x =130 , y = 10)

fullname=tk.Label(review,text="Enter Full Name:",width=20)
fullname.config(font=("Courier", 12))
fullname.place(x=180,y=110)

ipname = tk.Entry(review)  
ipname.place(x=400,y=110)

address=tk.Label(review,text="Enter Address:",width=20)
address.config(font=("Courier", 12))
address.place(x=180,y=160)

ipaddr = tk.Entry(review)  
ipaddr.place(x=400,y=160)

taste=tk.Label(review,text="Food Taste:",width=20)
taste.config(font=("Courier", 12))
taste.place(x=180,y=210)

taste_var = tk.IntVar(value=0)  # Variable to store selected value
one1_radio = tk.Radiobutton(review, text="1", variable=taste_var, value=1)
one1_radio.place(x=400, y=210)
two1_radio = tk.Radiobutton(review, text="2", variable=taste_var, value=2)
two1_radio.place(x=440, y=210)
thr1_radio = tk.Radiobutton(review, text="3", variable=taste_var, value=3)
thr1_radio.place(x=480, y=210)

# Food Quality radio buttons
quality = tk.Label(review, text="Food Quality", width=20, font=("Courier", 12))
quality.place(x=180, y=260)

quality_var = tk.IntVar(value=0)  # Variable to store selected value
one2_radio = tk.Radiobutton(review, text="1", variable=quality_var, value=1)
one2_radio.place(x=400, y=260)
two2_radio = tk.Radiobutton(review, text="2", variable=quality_var, value=2)
two2_radio.place(x=440, y=260)
thr2_radio = tk.Radiobutton(review, text="3", variable=quality_var, value=3)
thr2_radio.place(x=480, y=260)


detail=tk.Label(review,text="Explain your review",width=20)
detail.config(font=("Courier", 12))
detail.place(x=180,y=310)

ipdet = tk.Entry(review)  
ipdet.place(x=400,y=310)



 
tk.Button(review, text='Submit',width=20,bd= 0,bg='#2271F4',fg='white',).place(x=300,y=500) 
review.mainloop()