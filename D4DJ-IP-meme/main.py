from tkinter import *
from tkinter.ttk import *
import tempfile
import time
import webbrowser

ip = get('https://api.ipify.org').content.decode('utf8')
website = "https://www.youtube.com/watch?v=Fah9BwbyUEo"

webbrowser.open(website)
time.sleep(2)
print(ip)

root = Tk()
w = 1920
h = 100
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
print(ws, hs)
# x = (ws/2) - (w/2)
# y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, 0, 0))

ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

root.title("")
root.iconbitmap(default=ICON_PATH)

label = Label(root, text=str(ip), font="-weight bold -size 55").pack()

root.mainloop()
