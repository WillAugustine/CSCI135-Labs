# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:11:37 2022

@author: dgalarus
"""

from tkinter import *
from tkinter import ttk
import ExceptionalFractions as EM


def clickAdd():
    lblOperator.config(text="+")
    try:
        f,g = getFractions()
        setResult(EM.addFractions(f,g))
        lblError.config(text="")
    except Exception as e:
        lblError.config(text="ERROR: " + str(e))
    
def clickSubtract():
    lblOperator.config(text="-")
    try:
        f,g = getFractions()
        setResult(EM.subtractFractions(f,g))
        lblError.config(text="")
    except Exception as e:
        lblError.config(text="ERROR: " + str(e))
    
def clickMultiply():
    lblOperator.config(text="x")
    try:
        f,g = getFractions()
        setResult(EM.multiplyFractions(f,g))
        lblError.config(text="")
    except Exception as e:
        lblError.config(text="ERROR: " + str(e))
    
def clickDivide():
    lblOperator.config(text="÷")
    try:
        f,g = getFractions()
        setResult(EM.divideFractions(f,g))
        lblError.config(text="")
    except Exception as e:
        lblError.config(text="ERROR: " + str(e))
    
def getFractions():
    try:
        n1 = int(eNumerator1.get())
        d1 = int(eDenominator1.get())
        n2 = int(eNumerator2.get())
        d2 = int(eDenominator2.get())
    except:
        raise Exception("Invalid Fraction(s)")
    fracs = ( EM.makeFraction(n1,d1), EM.makeFraction(n2,d2) ) 
    return fracs
        
def setResult(f):
    n=f[0]
    d=f[1]
    lblResultNumerator.config(text=str(n))
    lblResultDenominator.config(text=str(d))
    

root = Tk()
root.title("Fraction Calculator")

frm = ttk.Frame(root, padding=10)
frm.grid()


fontHeader = ("Helvetica", 20, "bold")
fontInstructions = ("Helvetica", 12)
fontOperator = ("Helvetica", 16)
fontNumbers = ("Helvetica", 16)
fontDivideBar = ("Helvetica", 16, "bold")
fontButtonText = ("Helvetica", 16)

style = ttk.Style()
style.configure('op.TButton', font=fontButtonText, foreground="blue")

style = ttk.Style()
style.configure('err.TLabel', font=fontButtonText, foreground="blue")

ttk.Label(frm, text="Fraction Calculator", font=fontHeader).grid(column=0, row=0, columnspan=5)
ttk.Label(frm, text="Enter fractions and choose an operation\nto see the result.\n", font=fontInstructions).grid(column=0, row=1, columnspan=5)

eNumerator1 = ttk.Entry(frm, justify="right", width=5, font=fontNumbers)
eNumerator1.grid(column=0, row=2)
ttk.Label(frm, text="---------", font=fontDivideBar).grid(column=0, row=3)
eDenominator1 = ttk.Entry(frm, justify="right", width=5, font=fontNumbers)
eDenominator1.grid(column=0, row=4)

eNumerator1.insert(0,"1")
eDenominator1.insert(0,"2")

lblOperator = ttk.Label(frm, text="+", font=fontOperator, foreground="blue")
lblOperator.grid(column=1, row=3)

eNumerator2 = ttk.Entry(frm, justify="right", width=5, font=fontNumbers)
eNumerator2.grid(column=2, row=2)
ttk.Label(frm, text="---------", font=fontDivideBar).grid(column=2, row=3)
eDenominator2 = ttk.Entry(frm, justify="right", width=5, font=fontNumbers)
eDenominator2.grid(column=2, row=4)

eNumerator2.insert(0,"3")
eDenominator2.insert(0,"4")

ttk.Label(frm, text="=", font=fontOperator, foreground="blue").grid(column=3, row=3)

lblResultNumerator = ttk.Label(frm, text="5", font=fontNumbers)
lblResultNumerator.grid(column=4, row=2)
ttk.Label(frm, text="---------", font=fontDivideBar).grid(column=4, row=3)
lblResultDenominator = ttk.Label(frm, text="4", font=fontNumbers)
lblResultDenominator.grid(column=4, row=4)



lblError = ttk.Label(frm, text="", foreground="red")
lblError.grid(column=0, row=6, columnspan=5)

btnAdd = ttk.Button(frm, text="+", width=3, style="op.TButton", command=clickAdd)
btnAdd.grid(column=0, row=7)
btnSubtract = ttk.Button(frm, text="-", width=3, style="op.TButton", command=clickSubtract)
btnSubtract.grid(column=1, row=7)
btnMultiply = ttk.Button(frm, text="x", width=3, style="op.TButton", command=clickMultiply)
btnMultiply.grid(column=2, row=7)
btnDivide = ttk.Button(frm, text="÷", width=3, style="op.TButton", command=clickDivide)
btnDivide.grid(column=3, row=7)

root.mainloop()