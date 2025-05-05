"""
Programmer: Braxton Biggs
Assignment: Module 13 - Assignment
Date Completed: 4/23/25
Course: CITC 2391 - C01
Instructor: Martin Bell
"""
import tkinter as tk
import tkinter.messagebox

class MPGConvertor:
    def __init__(self):
        self.main_window = tk.Tk()

        self.head_frame = tk.Frame(self.main_window)
        self.gallons_frame = tk.Frame(self.main_window)
        self.miles_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        self.header_label = tk.Label(self.head_frame, text='Calculate Miles Per Gallon', font=('Arial', 12), justify='center')

        self.gallons_label = tk.Label(self.gallons_frame, text='Enter amount of fuel held (in gallons):')
        self.gallons_entry = tk.Entry(self.gallons_frame, width=10)
        self.miles_label = tk.Label(self.miles_frame, text='Enter number of miles driven on a full tank:')
        self.miles_entry = tk.Entry(self.miles_frame, width=10)

        # Pack the top frame widgets
        self.header_label.pack()
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        self.calc_button = tk.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tk.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.head_frame.pack()
        self.gallons_frame.pack()
        self.miles_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    def convert(self):
        miles = float(self.miles_entry.get())
        gallons = float(self.gallons_entry.get())
        mpg = miles / gallons

        tk.messagebox.showinfo('Results', str(mpg) + 'MPG.')

mpg_conv = MPGConvertor()