from tkinter import *
from tkinter import ttk
import pyshorteners
def convert():
    s = pyshorteners.Shortener().tinyurl.short(url.get())
    shorturl.set(s)
root = Tk()
root.title('URL Shortener')
frm = ttk.Frame(root, padding=10)
root.geometry('350x200')
root.resizable(False, False)
frm.grid()


url = StringVar()
shorturl = StringVar()

Label(root, text="Long URL").grid(row=2, padx=10, pady=10)
Entry(root, textvariable=url).grid(row=2, column=1, padx=10, pady=10)


ttk.Separator(root, orient=HORIZONTAL).grid(row=4, columnspan=10, padx=10, pady=10, sticky='ew')

def copyToClipboard(link):
    root.clipboard_clear()
    root.clipboard_append(link)


Label(root, text="Short URL").grid(row=6, padx=10, pady=10)
Entry(root, textvariable=shorturl).grid(row=6, column=1, padx=10, pady=10)
Button(root, text="Copy",  command=lambda:copyToClipboard(shorturl.get())).grid(row=6, column=2, padx=10, pady=10)


Button(root, text="Convert...", command=convert).grid(row=10, padx=10, pady=10)


root.mainloop()