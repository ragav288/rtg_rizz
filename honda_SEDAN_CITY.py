import tkinter as tk

from PIL import ImageTk,Image
from tkinter import PhotoImage


def create_horizontal_table(root, data):
    
    headers = ["VARIANT\n", "ENGINE\n", "AUTOMATIC/MANUAL\n",'MILEAGE\n','BOOT\nSPACE','DIMENSION\n','GROUND\nCLREARANCE\n','DIFFERENTIATING\nFEATURE','EX-SHOWROOM\nPRICE']
    for i, header in enumerate(headers):
        header_label = tk.Label(root, text=header, font=('Helvetica', 12, 'bold'))
        header_label.grid(row=0, column=i, padx=10, pady=5)


    for row_idx, car_data in enumerate(data):
        for col_idx, value in enumerate(car_data):
            cell_label = tk.Label(root, text=value, font=('Helvetica', 12))
            cell_label.grid(row=row_idx + 1, column=col_idx, padx=10, pady=5, sticky='w')

    
    


car_data = [
    ["city SV ", "1.0 TSI,113 KW power , 178 Nm Torque", "automatic","20","521 L","4541x1752x1507","179 mm", "fog light, Air conditioner , air purifier","12.1 L"],
    ["city v", "1.0 TSI,105 KW power , 178 Nm Torque","automatic", "22","412 L","4225x1760x1651","167 mm", "fog light , wireless charging and infoteinment system","13.22 L"],
    ["city VX", "1.5 TSI,110 KW power , 178 Nm Torque","automatic", "18","551 L","4233x1760x1612","168 mm", "fog light , wireless charging and infoteinment system , sun roof","14.1 L"],
    ["city ZX", "2 TSI,120 KW power , 180 Nm Torque","automatic", "23","545 L","4230x1760x1612","155 mm", "fog light , wireless charging and infoteinment system","14.99 L"],
    
]



root = tk.Tk()
root.title("honda sedan")
root.geometry('1500x1500')

root.configure(bg='#000000')

# Load the background image
background_image = PhotoImage(file="/Users/ragavgc/Desktop/Screenshot 2023-11-07 at 8.12.26 AM.png")

# Create a Label for the background image and set its position
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Call your create_horizontal_table function and other widgets
create_horizontal_table(root, car_data)

def back():
    root.destroy()
    import honda

back_button = tk.Button(root, text='back', command=back)
back_button.grid(row=9, column=4, columnspan=2)

#2560x1600

root.mainloop()
