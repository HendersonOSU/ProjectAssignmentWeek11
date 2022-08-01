from tkinter import *

TAX_RATE = 0.20
STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0


def computeTax():
    gross = float(grossEntry.get())
    numDependents = float(dependsEntry.get())
    taxableIncome = gross - STANDARD_DEDUCTION
    taxableIncome = taxableIncome - (DEPENDENT_DEDUCTION * numDependents)
    incomeTax = taxableIncome * TAX_RATE
    myText.set(incomeTax)


calculator = Tk()
myText = StringVar()
calculator.title("Taxation Calculator")
calculator.geometry("500x200")
Label(calculator, text="Gross income").grid(row=0)
Label(calculator, text="Dependents").grid(row=4)
Label(calculator, text="Total taxation:").grid(row=8)
result = Entry(calculator, text="", textvariable=myText).grid(
    row=8, column=1)

grossEntry = Entry(calculator)
dependsEntry = Entry(calculator)

grossEntry.grid(row=0, column=1)
dependsEntry.grid(row=4, column=1)

b = Button(calculator, text="Compute", command=computeTax)
b.grid(row=6, column=1, columnspan=2, rowspan=2)


mainloop()
