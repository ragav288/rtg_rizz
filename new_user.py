import tkinter as tk 
import random as r
from tkinter import messagebox
import csv

def button_click():
    mail=mail_entry.get()
   
    pwd=pwd_entry.get()
    pwd1=pwd1_entry.get()
    if pwd != pwd1:
        messagebox.showerror(title="sign up Failed", message="Check your password!")
    else:
        with open('RTG_acc_file.csv','a') as f:
            a=csv.writer(f)
            a.writerow([mail,pwd])
       
        messagebox.showinfo(title="sign up Successful", message="please login to your new account.")
        root2.destroy()
        import existing_user


bank_id = 0
k = True


root2 = tk.Tk()
root2.title("Sign Up Form")
root2.geometry("1000x1000")


pwd = tk.Label(root2, text="Password:" ,font = ("Arial",20))
pwd_entry = tk.Entry(root2, show="*")

pwd1 = tk.Label(root2, text=" Re-enter Password:" ,font = ("Arial",20))
pwd1_entry = tk.Entry(root2, show="")

mail = tk.Label(root2, text="Mail id:" , font = ("Arial",20))
mail_entry = tk.Entry(root2)

mail.pack(padx=20 , pady=20)
mail_entry.pack(padx=20 , pady=20)

pwd.pack(padx=20 , pady=20)
pwd_entry.pack(padx=20 , pady=20)

pwd1.pack(padx=20 , pady=20)
pwd1_entry.pack(padx=20 , pady=20)





login_button = tk.Button(root2, text="confirm", command = button_click , font = ("Arial",20))



login_button.pack(padx=20 , pady=20)



root2.mainloop()


