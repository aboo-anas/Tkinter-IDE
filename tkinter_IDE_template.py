import tkinter as tk


root = tk.Tk()
root.geometry('600x600')
root.title('Tkinter Simple IDE')

widget_frame = tk.Frame(root, bg='#272727')

widget_frame.pack_propagate(False)
widget_frame.configure(width=100)

widget_frame.pack(side=tk.LEFT, fill=tk.Y)



root.mainloop()
