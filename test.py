#!/usr/bin/python3
from tkinter import *
import tkinter as tk

####################### Corinci Deployment Function ########################
def corinci_deployment():
    corinci_win = tk.Toplevel(root)

    def close_window():
        corinci_win.destroy()
        button1.config(state='normal')

    button1.config(state='disable')

    corinci_win.protocol("WM_DELETE_WINDOW", close_window)

    corinci_win.title('Corinci Patch deployemnt')
    corinci_win.geometry('{}x{}'.format(300, 150))
    desc_title = Label(corinci_win, text='Corinci', width=45, height=1, bg="blue").pack()

    patch_name = Label(corinci_win, text='Patch Name :- ').place(x=0, y=30)
    patch_entry = Entry(corinci_win).place(x=100, y=30)

    targt_name = Label(corinci_win, text='Target :- ').place(x=0, y=60)
    target_entry = Entry(corinci_win).place(x=100, y=60)

    def reset_cor_window():
        corinci_win.destroy()
        button1.config(state='normal')

    submit_patch_button = Button(corinci_win, text ="Deploy").place(x=50, y=100)
    reset_patch_button = Button(corinci_win, text ="Reset", command=reset_cor_window).place(x=150, y=100)


####################### Adhoc Deployment Function ########################
def adhoc_deployment():
    adhoc_win = tk.Toplevel(root)

    def close_window():
        adhoc_win.destroy()
        button2.config(state='normal')

    button2.config(state='disable')

    adhoc_win.protocol("WM_DELETE_WINDOW", close_window)

    adhoc_win.title('Adhoc Patch deployemnt')
    adhoc_win.geometry('{}x{}'.format(300, 150))
    desc_title = Label(adhoc_win, text='Adhoc', width=45, height=1, bg="blue").pack()

    patch_name = Label(adhoc_win, text='Patch Name :- ').place(x=0, y=30)
    patch_entry = Entry(adhoc_win).place(x=100, y=30)

    targt_name = Label(adhoc_win, text='Target :- ').place(x=0, y=60)
    target_entry = Entry(adhoc_win).place(x=100, y=60)

    def reset_adc_window():
        adhoc_win.destroy()
        button2.config(state='normal')

    submit_patch_button = Button(adhoc_win, text ="Deploy").place(x=50, y=100)
    reset_patch_button = Button(adhoc_win, text ="Reset", command=reset_adc_window).place(x=150, y=100)



################################# Main ##########################################
root = Tk()
root.title('Model Definition')
root.geometry('{}x{}'.format(450, 260))

# create all of the main containers
title_frame = Frame(root, bg='blue', width=450, height=50)
empty1_frame = Frame(root, bg='white', width=450, height=20)
center_frame = Frame(root, bg='gray', width=450, height=50)
empty2_frame = Frame(root, bg='white', width=450, height=20)
button_frame = Frame(root, bg='blue', width=450, height=70)
empty3_frame = Frame(root, bg='white', width=450, height=20)
support_frame = Frame(root, bg='gray', width=450, height=20)
btm_frame = Frame(root, bg='white', width=450, height=100)
btm_frame2 = Frame(root, bg='lavender', width=450, height=60)


# -- layout all of the main containers -- #
title_frame.grid(row=0, sticky="ew")
empty1_frame.grid(row=1, sticky="ew")
center_frame.grid(row=2, sticky="ew")
empty2_frame.grid(row=3, sticky="ew")
button_frame.grid(row=4, sticky="ew")
empty3_frame.grid(row=5, sticky="ew")
support_frame.grid(row=6, sticky="ew")
# ---------------------------------

# -- Create Widgets for the Frame -- #
tool_title = Label(title_frame, text='Patch Deployment Tool', width=45, height=3, bg="blue", font=15)
#tool_title.pack()
tool_title.grid(row=0)

tool_description = Label(center_frame, text='Tool Description Should go here', width=45, height=3, bg='gray')
tool_description.pack()

button1 = Button(button_frame, text ="Corinci", width=15, height=4, command=corinci_deployment)
button1.grid(row=4, column=1)

button2 = Button(button_frame, text ="AdHoc", width=15, height=4, command=adhoc_deployment)
button2.grid(row=4, column=2)

button3 = Button(button_frame, text ="Special", width=15, height=4)
button3.grid(row=4, column=3)

support_label = Label(support_frame, text='Support:- saifn@hcl.com')
support_label.pack()
# ---------------------------------

root.mainloop()

##########################################################################################################
