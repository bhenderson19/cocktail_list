from tkinter import *

from cocktail_list import getCocktails

def enter():
    output = Tk()
    ingredients = e.get().replace(", ",",").split(",")
    output.title("Cocktails containing... "+e.get())
    cocktails = getCocktails(ingredients)
    for drink in cocktails:
        Label(output,text=drink).pack()

master = Tk()
master.title("Cocktail Search")
master.geometry("200x75")

Label(master,text="Enter Ingredients").pack()
e = Entry(master)
e.pack()
Button(master,text="Enter",command=enter).pack()

mainloop()