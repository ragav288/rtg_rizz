import tkinter as tk



def create_horizontal_table(root, data):
    
    headers = ["VARIANT", "ENGINE", "AUTOMATIC/MANUAL",'MILEAGE','BOOT SPACE','DIMENSION','GROUND CLREARANCE','DIFFERENTIATING FEATURE','EX-SHOWROOM PRICE']
    for i, header in enumerate(headers):
        header_label = tk.Label(root, text=header, font=('Helvetica', 12, 'bold'))
        header_label.grid(row=0, column=i, padx=10, pady=5)


    for row_idx, car_data in enumerate(data):
        for col_idx, value in enumerate(car_data):
            cell_label = tk.Label(root, text=value, font=('Helvetica', 12))
            cell_label.grid(row=row_idx + 1, column=col_idx, padx=10, pady=5, sticky='w')

    
    


car_data = [
    ["Kushaq Active", "1.0 TSI,85 KW power , 178 Nm Torque", "automatic","20","385 L","4225x1760x1612","155 mm", "fog light, Air conditioner , air purifier","11.59 L"],
    ["Kushaq Ambition", "1.0 TSI,85 KW power , 178 Nm Torque","automatic", "20","385 L","4225x1760x1612","155 mm", "fog light , wireless charging and infoteinment system","13.34 L"],
    ["Kushaq style", "1.0 TSI,85 KW power , 178 Nm Torque","automatic", "20","385 L","4225x1760x1612","155 mm", "fog light , wireless charging and infoteinment system , sun roof","15.79 L"],
    ["Kushaq Ambition", "1.5 TSI,110 KW power , 250 Nm Torque","automatic", "19","385 L","4225x1760x1612","155 mm", "fog light , wireless charging and infoteinment system","14.99 L"],
    ["Kushaq style", "1.5 TSI,110 KW power , 250 Nm Torque","automatic", "19","385 L","4225x1760x1612","155 mm", "fog light , wireless charging and infoteinment system , sun roof","17.79 L"],
]



root = tk.Tk()
root.title("Skoda SUV")






create_horizontal_table(root, car_data)

def back():
    root.destroy()
    import skoda
back_button = tk.Button(root, text = 'back', command = back)
back_button.grid(row=6, column=4, columnspan = 2)


root.mainloop()
