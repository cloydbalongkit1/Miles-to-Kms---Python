from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
window.minsize(width=100, height=50)

label_mile = Label(text="Mile:")
label_mile.config(padx=10, pady=10)
label_mile.grid(column=0, row=0)

user_input = Entry(width=15)
user_input.grid(column=1, row=0)

label_km = Label(text="Km:")
label_km.config(padx=10, pady=10)
label_km.grid(column=1, row=2)

label_answer = Label(text="Answer!")
label_answer.grid(column=2, row=2)

label_is_equal = Label(text='is equal to = ')
label_is_equal.grid(column=0, row=2)

def answer():
    input_user = float(user_input.get())
    mi_km = 1.6
    km = mi_km * input_user

    return label_answer.config(text=km)

button = Button(text="Calculate", command=answer)
button.grid(column=1, row=3)



window.mainloop()

