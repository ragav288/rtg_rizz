import tkinter as tk
root = tk.Tk()
root.title("Available brands")
root.geometry("1000x1000")
lbl=tk.Label(root,text = "SELECT YOUR CAR BRAND" , font = ("Bold Italic",30))
lbl.pack(padx=20 , pady =20)

ch = 0

choice = tk.IntVar()


button1 = tk.Button(root, text="Hyundai", command = lambda: hyundai() , padx=30 , pady=30)
button2 = tk.Button(root, text="Kia", command = lambda: kia() , padx=30 , pady=30)
button3 = tk.Button(root, text="Skoda", command = lambda: skoda() , padx=30 , pady=30)
button4 = tk.Button(root, text="Honda", command = lambda: honda() , padx=30 , pady=30)


button1.pack()
button2.pack()
button3.pack()
button4.pack()

def hyundai():
  root.destroy()
  import hyundai

def kia():
  root.destroy()
  import Kia

def skoda():
  root.destroy()
  import skoda

def honda():
  root.destroy()
  import honda


root.mainloop()
