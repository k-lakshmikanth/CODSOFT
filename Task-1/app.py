import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import json

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        
        self.tasks = []

        # Frame for tasks
        self.task_frame = tk.Frame(self.master)
        self.task_frame.pack(pady=10)

        # Load icons
        self.add_icon = Image.open(r"C:\Users\nokia\Desktop\CODSOFT\Task-1\resources\add_icon.png").resize((25, 25))
        self.add_icon = ImageTk.PhotoImage(self.add_icon)
        self.remove_icon = Image.open(r"C:\Users\nokia\Desktop\CODSOFT\Task-1\resources\remove_icon.png").resize((25, 25))
        self.remove_icon = ImageTk.PhotoImage(self.remove_icon)


        # Add task button 
        self.add_button = tk.Button(self.master, image=self.add_icon, command=self.add_task, borderwidth=0)
        self.add_button.pack()

        # Start auto-reloading tasks every 5 seconds
        self.reload_tasks()

    def add_task(self):
        # Entry field for task
        self.task_entry = tk.Entry(self.master, width=50)
        self.task_entry.pack(pady=10)
        if task:
            self.tasks.append(task)
            self.update_tasks_display()
            self.task_entry.delete(0, tk.END)
            self.save_tasks_to_file()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self, task_frame):
        task = task_frame.task_label.cget("text")
        self.tasks.remove(task)
        task_frame.destroy()
        self.save_tasks_to_file()

    def update_tasks_display(self):
        for task in self.tasks:
            task_frame = tk.Frame(self.task_frame)
            task_frame.pack(fill=tk.X)

            task_label = tk.Label(task_frame, text=task, width=40)
            task_label.pack(side=tk.LEFT, padx=(5, 0))

            remove_button = tk.Button(task_frame, image=self.remove_icon, command=lambda frame=task_frame: self.remove_task(frame), borderwidth=0)
            remove_button.pack(side=tk.RIGHT, padx=(0, 5))

            task_frame.task_label = task_label
            self.task_frame.update_idletasks()

    def save_tasks_to_file(self):
        with open(r"Task-1\data\tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks_from_file(self):
        try:
            with open(r"Task-1\data\tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            pass

    def reload_tasks(self):
        self.load_tasks_from_file()
        self.update_tasks_display()
        self.master.after(5000, self.reload_tasks)

def main():
    root = tk.Tk()
    todo_app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
