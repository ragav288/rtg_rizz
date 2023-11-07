import tkinter as tk
root = tk.Tk()

root.title("RTG car dealership online booking")

root.geometry("1000x1000")

ch = 0

choice = tk.IntVar()

radio1 = tk.Radiobutton(root, text="SIGN IN", variable=choice, value=1 , font = ("Bold Italic", 50))
radio2 = tk.Radiobutton(root, text="SIGN UP", variable=choice, value=2 , font = ("Bold Italic" , 50))

radio1.pack(padx=20 , pady=20)
radio2.pack(padx=20 , pady=20)

def process_choice():

  ch = choice.get()
  if ch == 1:
        root.destroy()
        import existing_user
        
  elif ch == 2:
        root.destroy()
        import new_user

button = tk.Button(root, text="Enter", command=lambda: process_choice(), font = ("Bold Italic" , 50))
button.pack(padx=20 , pady=20)
        

root.mainloop()
