import tkinter as tk


root = tk.Tk()
root.geometry('600x600')
root.title('Tkinter Simple IDE')

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

#Create a button for running codes
run_btn = tk.Button(widget_frame, text='Run code', bg='#272727', fg='lime', font=('Bold', 15),
                    command= lambda: run_code(tex_pad.get('1.0', tk.END)))
run_btn.pack(pady= 5, fill=tk.X)

#create a button for clearing inputs
clear_btn = tk.Button(widget_frame, text='Clear', bg='#272727', fg='red', font=('Bold', 15),
                      command= btn_clear)
clear_btn.pack(pady= 5, fill=tk.X)

#Create Widget buttons
wn = 0
for i in Widgets:

    btn = tk.Button(widget_frame, text=Widgets[wn][0], bg='#272727', fg='yellow', font=('Bold', 13),
                 command= lambda wn = wn: insert_widget_code(Widgets[wn][1]))
    btn.pack(pady= 5, fill=tk.X)
    wn+=1


root.mainloop()
