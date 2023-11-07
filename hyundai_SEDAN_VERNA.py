import tkinter as tk



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
    ["verna EX", "1.0 TSI,113 KW power , 178 Nm Torque", "automatic","20","521 L","4541x1752x1507","179 mm", "fog light, Air conditioner , air purifier","11.34 L"],
    ["verna S ", "1.0 TSI,105 KW power , 178 Nm Torque","automatic", "22","412 L","4225x1760x1651","167 mm", "fog light , wireless charging and infoteinment system","12.22 L"],
    ["verna SX", "1.5 TSI,110 KW power , 180 Nm Torque","automatic", "18","551 L","4233x1760x1612","168 mm", "fog light , wireless charging and infoteinment system , sun roof","13.1 L"],
    ["verna SX plus", "2 TSI,120 KW power , 185 Nm Torque","automatic", "23","545 L","4230x1760x1612","155 mm", "fog light , wireless charging and infoteinment system","13.99 L"],
    
]



root = tk.Tk()
root.title("Hyundai MPV")






create_horizontal_table(root, car_data)

def back():
    root.destroy()
    import hyundai
back_button = tk.Button(root, text = 'back', command = back)
back_button.grid(row=6, column=4, columnspan = 2)


root.mainloop()

