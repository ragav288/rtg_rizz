import tkinter as tk

root= tk.Tk()

root.title("Kia")


root.geometry("1000x1000")
lbl=tk.Label(root,text = "SELECT YOUR SEGMENT" , font = ("Bold Italic",30))
lbl.pack(padx=20 , pady =20)

ch = 0

choice = tk.IntVar()

radio1 = tk.Radiobutton(root, text="MPV", variable=choice, value=1 , font = ("Bold Italic", 20))
radio2 = tk.Radiobutton(root, text="SUV", variable=choice, value=2 , font = ("Bold Italic", 20))


radio1.pack(padx=20 , pady=20)
radio2.pack(padx=20 , pady=20)

def process_choice():

  ch = choice.get()
  if ch == 1:
        root.destroy()
        import kia_MPV_CARENS
        
  elif ch == 2:
        root.destroy()
        import kia_SUV_SELTOS
button = tk.Button(root, text="Enter", command=lambda: process_choice(), font = ("Bold Italic" , 50))
button.pack(padx=20 , pady=20)


def back():
    root.destroy()
    import car_brand
back_button = tk.Button(root, text = 'back', command = back)
back_button.pack()



root.mainloop()
