import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from idlelib.colorizer import ColorDelegator
from idlelib.percolator import Percolator
from tkinter import filedialog

root = tk.Tk()
root.geometry('600x600')
root.title('Tkinter Simple IDE')

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.py',
                                    filetypes=[
                                        ('Python file', '.py'),
                                        ('Text file', '.txt'),
                                        ('HTML file', '.html'),
                                        ('All files', '.*')
                                    ])
    if file is None:
        return
    filetext = str(tex_pad.get('1.0', tk.END))
    file.write(filetext)
    file.close()

def insert_widget_code(code):
    tex_pad.insert(tk.INSERT, code)

def run_code(code):
    return exec(code)

def btn_clear():
    tex_pad.delete('1.0', tk.END)

Widgets =[
    ["Create\nWindow", "import tkinter as tk\n\nroot = tk.Tk()\nroot.title('My Window')\nroot.geometry('600x600')\n\nroot.mainloop()"],
    ["Frame", "frm_1 = tk.Frame(root)\nfrm_1.pack()"],
    ["Label", "label_1 = tk.Label(root, text='Hello World')\nlabel_1.pack()"],
    ["Entry", "entry1 = tk.Entry(root)\nentry1.pack()"],
    ["Text", "text1 = tk.Text(root)\ntext1.pack()"],
    ["ListBox", "l_box = tk.Listbox(root)\nl_box.pack()"],
    ["Button", "btn = tk.Button(root, text= 'Hello World')\nbtn.pack()"],
    ["Checkbutton", "Check_btn = tk.Checkbutton(root, text='Hello World')\ncheck_btn.pack()"],
    ["Radiobuton", "Radio_btn = tk.Radiobutton(root, text='Hello World')\nRadio_btn.pack()"],
    ["Menu", "menu1 = tk.Menu(root)\nmenu1.add_command(label = 'Menu')\nroot.config(menu=menu1)"],
    ["Scale", "scale1 = tk.Scale(root, from_=0, to=100)\nscale1.pack()"],
    ["Scrollbar", "sb =tk.Scrollbar(root)\nsb.pack()"]
]

widget_frame = tk.Frame(root, bg='#272727')

widget_frame.pack_propagate(False)
widget_frame.configure(width=100)

widget_frame.pack(side=tk.LEFT, fill=tk.Y)

#Create buttons
run_btn = tk.Button(widget_frame, text='Run code', bg='#272727', fg='lime', font=('Bold', 15),
                    command= lambda: run_code(tex_pad.get('1.0', tk.END)))
run_btn.pack(pady= 5, fill=tk.X)

clear_btn = tk.Button(widget_frame, text='Clear', bg='#272727', fg='red', font=('Bold', 15),
                      command= btn_clear)
clear_btn.pack(pady= 5, fill=tk.X)

btn1 = tk.Button(widget_frame, text=Widgets[0][0], bg='#272727', fg='yellow', font=('Bold', 13),
                 command= lambda: insert_widget_code(Widgets[0][1]))
btn1.pack(pady= 5, fill=tk.X)

btn2 = tk.Button(widget_frame, text=Widgets[1][0], bg='#272727', fg='yellow', font=('Bold', 13),
                 command= lambda: insert_widget_code(Widgets[1][1]))
btn2.pack(pady= 5, fill=tk.X)

btn3 = tk.Button(widget_frame, text=Widgets[2][0], bg='#272727', fg='yellow', font=('Bold', 13),
                 command= lambda: insert_widget_code(Widgets[2][1]))
btn3.pack(pady= 5, fill=tk.X)

btn4 = tk.Button(widget_frame, text=Widgets[3][0], bg='#272727', fg='yellow', font=('Bold', 13),
                 command= lambda: insert_widget_code(Widgets[3][1]))
btn4.pack(pady= 5, fill=tk.X)

btn5 = tk.Button(widget_frame, text=Widgets[4][0], bg='#272727', fg='yellow', font=('Bold', 13),
                 command= lambda: insert_widget_code(Widgets[4][1]))
btn5.pack(pady= 5, fill=tk.X)

btn6 = tk.Button(widget_frame, text=Widgets[5][0], bg='#272727', fg='yellow', font=('Bold', 13),
                 command= lambda: insert_widget_code(Widgets[5][1]))
btn6.pack(pady= 5, fill=tk.X)

btn7 = tk.Button(widget_frame, text=Widgets[6][0], bg='#272727', fg='yellow', font=('Bold', 13),
                 command= lambda: insert_widget_code(Widgets[6][1]))
btn7.pack(pady= 5, fill=tk.X)

btn8 = tk.Button(widget_frame, text=Widgets[7][0], bg='#272727', fg='yellow', font=('Bold', 13),
                 command= lambda: insert_widget_code(Widgets[7][1]))
btn8.pack(pady= 5, fill=tk.X)

btn9 = tk.Button(widget_frame, text=Widgets[8][0], bg='#272727', fg='yellow', font=('Bold', 13),
                 command= lambda: insert_widget_code(Widgets[8][1]))
btn9.pack(pady= 5, fill=tk.X)

btn10 = tk.Button(widget_frame, text=Widgets[9][0], bg='#272727', fg='yellow', font=('Bold', 13),
                  command= lambda: insert_widget_code(Widgets[9][1]))
btn10.pack(pady= 5, fill=tk.X)

btn11 = tk.Button(widget_frame, text=Widgets[10][0], bg='#272727', fg='yellow', font=('Bold', 13),
                  command= lambda: insert_widget_code(Widgets[10][1]))
btn11.pack(pady= 5, fill=tk.X)

btn12 = tk.Button(widget_frame, text=Widgets[11][0], bg='#272727', fg='yellow', font=('Bold', 13),
                  command= lambda: insert_widget_code(Widgets[11][1]))
btn12.pack(pady= 5, fill= tk.X)

#create a text area
main_frame = tk.Frame(root)

tex_pad = ScrolledText(main_frame, height=100, font=('Comic Sans MS', 12), bd=10, relief="raised")
tex_pad.pack(fill=tk.BOTH)

#Add save menu
menubar = tk.Menu(root)
filemenu =tk.Menu(menubar, tearoff=False)
filemenu.add_command(label="Save program", command= lambda: saveFile())
filemenu.add_separator()
filemenu.add_command(label="Exit", command= quit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

Percolator(tex_pad).insertfilter(ColorDelegator())

main_frame.pack(side=tk.LEFT, fill=tk.Y)


root.mainloop()