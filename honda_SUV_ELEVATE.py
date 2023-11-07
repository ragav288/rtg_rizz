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
    ["Elevate SV", "1.5 i-VTEC with VTC,89 KW power , 145 Nm Torque", "manual","15.31","458 L","4312x1790x1650","220 mm", "fog light, Air conditioner , air purifier","11.08 L"],
    ["Elevate V", "1.5 i-VTEC with VTC,89 KW power , 145 Nm Torque","manual", "15.31","458 L","4312x1790x1650","220 mm", "fog light , wireless charging and infoteinment system","12.19 L"],
    ["Elevate VX", "1.5 i-VTEC with VTC,89 KW power , 145 Nm Torque","manual", "15.31","458 L","4312x1790x1650","220 mm", "fog light , wireless charging and infoteinment system , sun roof","13.58 L"],
    ["Elevate ZX", "1.5 i-VTEC with VTC,89 KW power , 145 Nm Torque","manual", "15.31","458 L","4312x1790x1650","220 mm", "fog light , wireless charging and infoteinment system , sun roof , nitro booster","14.98 L"],
    ["Elevate V", "1.5 i-VTEC with VTC,89 KW power , 145 Nm Torque", "Automatic","16.92","458 L","4312x1790x1650","220 mm", "fog light, Air conditioner , air purifier","13.29 L"],
    ["Elevate VX", "1.5 i-VTEC with VTC,89 KW power , 145 Nm Torque", "Automatic","16.92","458 L","4312x1790x1650","220 mm", "fog light, Air conditioner , air purifier , sun roof","14.69 L"],
    ["Elevate ZX", "1.5 i-VTEC with VTC,89 KW power , 145 Nm Torque", "Automatic","16.92","458 L","4312x1790x1650","220 mm", "fog light, Air conditioner , air purifier , sun roof , nitro boosters","16.08 L"],
    
]




root = tk.Tk()
root.title("honda SUV")
root.geometry('1500x1500')
root.configure(bg='#000000')

# Load the background image
background_image = PhotoImage(file="/Users/ragavgc/Desktop/Screenshot 2023-11-06 at 2.18.53 PM.png")

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

root.mainloop()
