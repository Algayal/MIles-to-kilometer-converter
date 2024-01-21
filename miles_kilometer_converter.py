"""Module creates a desktop application that converts miles into kilometers"""
from tkinter import Button, Entry, Label, Tk


class MilesToKmConverter:
    """Miles to kilometers desktop application"""

    def __init__(self):
        self.miles_label = None
        self.equal_label = None
        self.kilometer_label = None
        self.input_entry = None
        self.initialize_window()
        self.labels()
        self.window.mainloop()
        self.window.mainloop()

    def initialize_window(self):
        """ "Create an empty window, add an entry field and a button"""

        self.window = Tk()
        self.window.title("Mile to Km Converter")
        self.window.config(padx=20, pady=20)

        self.entry_field()
        self.button = Button(text="Calculate", command=self.button_clicked)
        self.button.grid(column=3, row=5)

    def entry_field(self):
        """Create an empty entry field"""
        self.input_entry = Entry(width=10)
        self.input_entry.grid(column=3, row=0)

    def labels(self):
        """Create all the labels"""
        self.miles_label = Label(text="Miles")
        self.miles_label.grid(column=5, row=0)

        self.equal_label = Label(text="is equal to")
        self.equal_label.grid(column=0, row=3)

        self.result_label = Label(text="0")
        self.result_label.grid(column=3, row=3)

        self.kilometer_label = Label(text="Km")
        self.kilometer_label.grid(column=6, row=3)

    def converter(self, miles):
        """Mathematical operation for converting miles to km"""
        km = miles * 1.60934
        self.result_label.config(text=round(km, 1))

    def button_clicked(self):
        """Obtaining the user's input and inserting it into the converter function"""
        user_input = float(self.input_entry.get())
        self.converter(user_input)
