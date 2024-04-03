import tkinter as tk
from hashlib import new
from tkinter import messagebox
from datetime import datetime
import json
from PIL import Image, ImageTk

generate_id = lambda:new("sha256", datetime.now().isoformat().encode()).hexdigest()

def try_except(func):
    def inner(*args,**kwargs):
        try:
            return func(*args,**kwargs)
        except Exception as e:
            pass
    return inner


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")  
        self.master.geometry("400x500")   
        self.master.resizable(True, True)
        self.APP_NAME = tk.Label(self.master, text="To-Do List", width=30, font=("Arial", 25))
        self.APP_NAME.pack(side=tk.TOP, padx=10)

        with open(r"Task-1\data\tasks.json") as f:
            self.tasks = json.load(f)        

        # Load icons
        self.add_icon = Image.open(r"Task-1\resources\add_icon.png").resize((25, 25))
        self.add_icon = ImageTk.PhotoImage(self.add_icon)

        self.remove_icon = Image.open(r"Task-1\resources\remove_icon.png").resize((25, 25))
        self.remove_icon = ImageTk.PhotoImage(self.remove_icon)

        self.edit_icon = Image.open(r"Task-1\resources\edit_icon.png").resize((25, 25))
        self.edit_icon = ImageTk.PhotoImage(self.edit_icon)

        self.nav_frame = tk.Frame(self.master)
        self.nav_frame.pack(side=tk.TOP,pady=10)

        self.add_button = tk.Button(self.nav_frame,image=self.add_icon ,borderwidth=0, command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.task_frame = tk.Frame(self.master)
        self.task_frame.pack(pady=5)

        self.Reload_Frame()

    def add_task(self):
        id = generate_id()
        self.update_task(id)

    def update_task(self,id):
        self.edit_task(id)

    def edit_task(self,id):
        def get_entry_value(id):
            value = entry.get()
            if value:
                self.tasks[id] = {"task":value,"status":"To Do"}
                new_window.destroy()
                self.Reload_Frame()
            else:
                messagebox.showwarning("Warning", "Please enter a task.")
                
        new_window = tk.Tk()
        new_window.title("Edit Task")
        new_window.geometry("300x100")
        entry_label = tk.Label(new_window, text="Enter the Task:")
        entry_label.pack()
        entry = tk.Entry(new_window,width=50)
        entry.pack()
        submit_button = tk.Button(new_window, text="Submit", command=lambda:get_entry_value(id))
        submit_button.pack()
        new_window.mainloop()
              


    def remove_task(self, id):
        self.tasks.pop(id)
        self.Reload_Frame()

    @try_except
    def Reload_Frame(self):
        for widget in self.task_frame.winfo_children():
            widget.destroy()    

        for id, task in self.tasks.items():
            frame = tk.Frame(self.task_frame)
            frame.pack(side=tk.TOP)

            # add a drop down menu for status
            status = tk.StringVar(value=task["status"])
            status_menu = tk.OptionMenu(frame, status, "To Do", "In Progress", "Done", command=lambda value, id=id: update_status(value, id))
            status_menu.config(width=12)
            status_menu.pack(side=tk.LEFT, padx=2)

            # add task label to frame
            task_label = tk.Label(frame, text=task["task"], width=20)
            task_label.pack(side=tk.LEFT, padx=10)

            # add Remove Button to frame
            remove_button = tk.Button(frame,image=self.remove_icon ,borderwidth=0, command=lambda id=id: self.remove_task(id))
            remove_button.pack(side=tk.RIGHT, padx=2)

            # add Edit Button to frame
            edit_button = tk.Button(frame,image=self.edit_icon ,borderwidth=0, command=lambda id=id: self.update_task(id))
            edit_button.pack(side=tk.RIGHT, padx=2)

            frame.task_label = task_label
            self.task_frame.update_idletasks()
        
        self.save_tasks()

        def update_status(value, id):
            self.tasks[id]["status"] = value
            self.Reload_Frame()    


    def save_tasks(self):
        with open(r"Task-1\data\tasks.json", "w") as f:
            json.dump(self.tasks, f)


root = tk.Tk()
app = App(root)
root.mainloop()