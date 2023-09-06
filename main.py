from tkinter import *


def miles_to_km():
    miles = miles_input.get()
    km = format(1.6 * float(miles), "0.2f")
    killom_label.config(text=f"{km}")


window = Tk()
window.title("Miles to km convertor")
window.minsize(width=200, height=200)
window.config(padx=80, pady=80)

enter_miles = Label(text="Enter miles")
enter_miles.grid(column=0, row=0)
miles_input = Entry()
miles_input.config(width=10)
miles_input.grid(column=1, row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)
is_equal_to_label = Label(text="is equal to ")
is_equal_to_label.grid(column=0, row=1)

killom_label = Label(text="0")
killom_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


btn = Button(text="Calculate", command=miles_to_km)

btn.grid(column=1, row=2)


window.mainloop()
