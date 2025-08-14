import pyautogui as py
import tkinter as tk
import time 
import colour
root = tk.Tk()
root.geometry('500x300')
root.attributes('-topmost',1)
root.attributes('-toolwindow',1)
# py.moveTo(int(root.winfo_screenwidth())/2,int(root.winfo_screenheight())/2) 
font = ('courier',30)
labelhex = tk.Label(root,text='hex',font = font,bg='#062e32',fg='white')
labelrgb = tk.Label(root,text='rgb',font = font,bg='#062e32',fg='white')
labelhex.pack(expand=True,fill='x')
labelrgb.pack(expand=True,fill='x')

while True:
    root.update()
    pos = py.position()
    rgb = py.pixel(pos.x,pos.y)
    Hex = colour.rgb2hex((i/255 for i in rgb))
    labelhex.config(text=Hex)
    labelrgb.config(text=rgb)
    print(rgb)
    root.config(bg=Hex)

    def b(e):{
        open('color.yml','a+t').write(f'\nhex-color: "{Hex}"\nrgb-color: ({[f'{i},' for i in rgb]})'),
        labelhex.config(text=f"copied"),
        labelrgb.config(text=f"copied"),
        root.update(),
        time.sleep(1),
        
    }
        
    root.bind('c',b)
















