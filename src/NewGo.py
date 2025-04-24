import customtkinter as cc
import Flowsheet as fl

import pickle
from tkinter import filedialog

cc.set_appearance_mode('system ')
cc.set_default_color_theme('blue')



## Loading screen to begin

root = cc.CTk()

root.geometry("600x400")
root.title('Menu')

homepageframe = cc.CTkFrame(master=root)
homepageframe.place(relx = 0.5, rely=0.5 , anchor = 'center')




global CourseList
CourseList = []


# butframe = cc.CTkFrame(master = root, height = 40)
# butframe.pack(fill = 'x', side = 'top', pady  =5 )

# cellframe = cc.CTkFrame(master = root)
# cellframe.pack(fill = 'both', expand = True, pady = 5)








new_project_button = cc.CTkButton(homepageframe, text = 'New Project')
#Work out how to save and load course information!
load_project_button = cc.CTkButton(homepageframe, text  = 'Load Project')

new_project_button.pack(pady=2.5)
load_project_button.pack(after = new_project_button ,pady=2.5)



root.mainloop()





