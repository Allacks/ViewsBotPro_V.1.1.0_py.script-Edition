import os
import time
import webbrowser
from tkinter import *
import threading

chrome_browser = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

GUI = Tk()
GUI.title("ViewsBot")
GUI.geometry("275x50")

Link = Entry(GUI,
            width=25,
            bg='red',
            fg='white')
Link.grid(row=0, column=0)

def process():
    webbrowser.get(chrome_browser).open(Link.get())


def thread1():
    threading.Thread(target=process).start()

def main():
   time.sleep(21)
   os.system("taskkill /im chrome.exe /f")
   time.sleep(2)
   thread1()
   time.sleep(25)
   os.system("taskkill /im chrome.exe /f")
   time.sleep(3)
   thread1()
   time.sleep(23)
   os.system("taskkill /im chrome.exe /f")
   thread1()
   main()

def thread2():
    threading.Thread(target=main).start()

def split():
    thread1()
    thread2()


startbutton = Button(GUI, text="Start Bot", command=split, bg='green2', fg='black')
startbutton.grid(row=0, column=4)


GUI['bg'] = 'black'
GUI.mainloop()
