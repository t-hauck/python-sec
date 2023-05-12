import webbrowser
from tkinter import *

root = Tk()


root.title("Abrir Browser")
root.geometry("300x200")

def search():
    webbrowser.open("https://start.duckduckgo.com/")
    
mySearch = Button(root, text="Abrir Pesquisa", command=search).pack(pady=20) # pady = posição do botão
root.mailloop()
