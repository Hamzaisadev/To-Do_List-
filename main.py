
import customtkinter as CTk
import tkinter as tk
import CTkListbox as ctklb
import CTkMessagebox
from PIL import Image
import webbrowser as wb

linkdin = CTk.CTkImage(Image.open('Resources/Images/LinkedIn.png'),
                       size=(50, 50))

github_link =CTk.CTkImage(Image.open('Resources/Images/GitHub.png'),
                      size=(70, 50))

todo_list = CTk.CTk()

todo_list.geometry("400x500")
todo_list.title("To-Do List")
todo_list.resizable(False, False)

CTk.set_default_color_theme("Resources/red.json")
CTk.set_appearance_mode("dark")

mode = "dark"


def change_theme():
  global mode
  if mode == "dark":
    CTk.set_appearance_mode("light")
    mode = "light"
    theme_button.configure(text="Light Mode")
  elif mode == "light":
    CTk.set_appearance_mode("dark")
    mode = "dark"
    theme_button.configure(text="Dark Mode")


theme_button = CTk.CTkSwitch(todo_list, text="Dark Mode", command=change_theme)

theme_button.pack
theme_button.place(x=286, y=10)

task_list = []


def github():
  wb.open_new_tab("https://github.com/hamzaisadev")


def linkDin():
  wb.open_new_tab("https://www.linkedin.com/in/hamzaisadev/")


def add_task():
  task = task_entry.get()
  if len(task) == 0:
    CTkMessagebox.CTkMessagebox(title="info", message="Please enter a task")
  else:
    task_entry.delete(0, tk.END)
    task_list.append(task)
    update_task_list()


def update_task_list():
  task_listbox.delete(0, tk.END)
  for task in task_list:
    task_listbox.insert(tk.END, task)


def delete_task():

  try:
    the_task = task_listbox.get(task_listbox.curselection())
    if the_task in task_list:
      task_list.remove(the_task)
      update_task_list()
  except:
    CTkMessagebox.CTkMessagebox(
        title="error", message="Can't Delete!! select something to delete")


def new_day():
  global task_list
  task_list = []
  update_task_list()


def exit():
  todo_list.destroy


to_do_label = CTk.CTkLabel(todo_list,
                           text="The TO-Do List",
                           text_color="red",
                           font=("Helvetica", 30, "bold"))
to_do_label.pack
to_do_label.place(x=10, y=10)

task_entry_label = CTk.CTkLabel(todo_list,
                                text="Enter Task :",
                                font=("Helvetica", 15, "bold"))

task_entry_label.pack
task_entry_label.place(x=10, y=70)

task_list_label = CTk.CTkLabel(todo_list,
                               text="Tasks :",
                               font=("Helvetica", 15, "bold"))

task_list_label.pack
task_list_label.place(x=170, y=140)

task_entry = CTk.CTkEntry(master=todo_list,
                          placeholder_text="Enter Task",
                          width=382,
                          height=35,
                          font=("Helvetica", 15, "bold"))

task_entry.pack()
task_entry.place(x=10, y=100)

task_listbox = ctklb.CTkListbox(todo_list, width=200, height=200)

task_listbox.pack()
task_listbox.place(x=170, y=170)

add_task_btn = CTk.CTkButton(master=todo_list,
                             text="Add Task",
                             height=35,
                             corner_radius=100,
                             font=("Helvetica", 15, "bold"),
                             command=add_task)

add_task_btn.pack()
add_task_btn.place(x=10, y=190)

delete_task_btn = CTk.CTkButton(master=todo_list,
                                height=35,
                                corner_radius=100,
                                font=("Helvetica", 15, "bold"),
                                text="Delete Task",
                                command=delete_task)

delete_task_btn.pack()
delete_task_btn.place(x=10, y=240)

next_day_btn = CTk.CTkButton(master=todo_list,
                             height=35,
                             corner_radius=100,
                             font=("Helvetica", 15, "bold"),
                             text="Next Day")

next_day_btn.pack()
next_day_btn.place(x=10, y=290)

exit_btn = CTk.CTkButton(master=todo_list,
                         height=35,
                         corner_radius=100,
                         font=("Helvetica", 15, "bold"),
                         text="Exit",
                         command=exit)

exit_btn.pack()
exit_btn.place(x=10, y=340)

LinkedIn_btn = CTk.CTkButton(master=todo_list,
                             height=5,
                             width=1,
                             fg_color="transparent",
                             corner_radius=1000,
                          
                             text="",
                             image=linkdin,
                             command=linkDin)

LinkedIn_btn.pack()
LinkedIn_btn.place(x=10, y=440)




github_btn = CTk.CTkButton(master=todo_list,
                             height=5,
                             width=5,
                             fg_color="transparent",
                             corner_radius=1000,
                          
                             text="",
                             image=github_link,
                             command=linkDin)

github_btn.pack()
github_btn.place(x=80, y=440)






thanks_label = CTk.CTkLabel(todo_list,
                            text="Important links",
                            font=(
                                "Helvetica",
                                15,"bold",
                            ))
thanks_label.pack()
thanks_label.place(x=10, y=400)
todo_list.mainloop()
