import tkinter as tk
from tkinter import messagebox
import time

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("500x550")

# Create frames for layout
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

frame_active_tasks = tk.LabelFrame(root, text="Active Tasks")
frame_active_tasks.pack(pady=10, fill="both", expand=True)

frame_history = tk.LabelFrame(root, text="Completed Tasks")
frame_history.pack(pady=10, fill="both", expand=True)

frame_pending_tasks = tk.LabelFrame(root, text="Pending Tasks")
frame_pending_tasks.pack(pady=10, fill="both", expand=True)

# Task input widgets
task_label = tk.Label(frame_input, text="Enter Task:")
task_label.pack(side=tk.LEFT)

task_entry = tk.Entry(frame_input, width=25)
task_entry.pack(side=tk.LEFT)

duration_label = tk.Label(frame_input, text="Duration (min):")
duration_label.pack(side=tk.LEFT)

duration_entry = tk.Entry(frame_input, width=10)
duration_entry.pack(side=tk.LEFT)

# Data structures for managing tasks
task_metadata = {}  # Stores task details with task_name as the key
active_tasks = []   # List to store active task frames

# Function to add a task
def add_task():
    task_name = task_entry.get().strip()
    duration = duration_entry.get().strip()

    if not task_name or not duration.isdigit():
        messagebox.showwarning("Input Error", "Please enter both a valid task name and duration!")
        return

    if task_name in task_metadata:
        messagebox.showwarning("Duplicate Task", "Task already exists!")
        return

    task_frame = tk.Frame(frame_active_tasks)
    task_frame.pack(pady=5, fill=tk.X)

    task_checkbox = tk.Checkbutton(task_frame, command=lambda: mark_completed(task_frame, task_name))
    task_checkbox.pack(side=tk.LEFT)

    task_label = tk.Label(task_frame, text=f"{task_name} - {duration} minutes")
    task_label.pack(side=tk.LEFT)

    delete_button = tk.Button(task_frame, text="Delete", command=lambda: delete_task(task_frame, task_name))
    delete_button.pack(side=tk.RIGHT)

    active_tasks.append(task_frame)
    task_metadata[task_name] = {
        "frame": task_frame,
        "duration": int(duration),
        "start_time": time.time()
    }

    task_entry.delete(0, tk.END)
    duration_entry.delete(0, tk.END)

# Function to mark a task as completed
def mark_completed(task_frame, task_name):
    task_frame.pack_forget()
    if task_frame in active_tasks:
        active_tasks.remove(task_frame)
    task_metadata.pop(task_name, None)

    history_label = tk.Label(frame_history, text=f"✅ {task_name}")
    history_label.pack(pady=5)

# Function to delete a task
def delete_task(task_frame, task_name):
    task_frame.pack_forget()
    if task_frame in active_tasks:
        active_tasks.remove(task_frame)
    task_metadata.pop(task_name, None)

# Function to check pending tasks
def check_pending_tasks():
    current_time = time.time()
    overdue_tasks = []

    for task_name, details in list(task_metadata.items()):
        elapsed_time = (current_time - details["start_time"]) / 60
        if elapsed_time > details["duration"]:
            overdue_tasks.append(task_name)

    for task_name in overdue_tasks:
        task_frame = task_metadata[task_name]["frame"]
        task_frame.pack_forget()
        if task_frame in active_tasks:
            active_tasks.remove(task_frame)

        pending_label = tk.Label(frame_pending_tasks, text=f"⚠ Pending: {task_name}")
        pending_label.pack(pady=5)

        task_metadata.pop(task_name, None)

    root.after(1000, check_pending_tasks)  # Check every second

# Function to sort tasks by name
def sort_by_name():
    sorted_tasks = sorted(task_metadata.items(), key=lambda x: x[0].lower())
    update_task_ui(sorted_tasks)

# Function to update the UI with sorted tasks
def update_task_ui(sorted_tasks):
    # Clear existing tasks
    for frame in active_tasks:
        frame.pack_forget()

    active_tasks.clear()

    # Re-add tasks in sorted order
    for task_name, details in sorted_tasks:
        task_frame = tk.Frame(frame_active_tasks)
        task_frame.pack(pady=5, fill=tk.X)

        task_checkbox = tk.Checkbutton(task_frame, command=lambda t=task_name: mark_completed(task_frame, t))
        task_checkbox.pack(side=tk.LEFT)

        task_label = tk.Label(task_frame, text=f"{task_name} - {details['duration']} minutes")
        task_label.pack(side=tk.LEFT)

        delete_button = tk.Button(task_frame, text="Delete", command=lambda t=task_name: delete_task(task_frame, t))
        delete_button.pack(side=tk.RIGHT)

        active_tasks.append(task_frame)
        task_metadata[task_name]["frame"] = task_frame  # Update frame reference

# Button to add tasks
add_button = tk.Button(frame_input, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

# Button to sort tasks by name
sort_name_button = tk.Button(frame_active_tasks, text="Sort by Name", command=sort_by_name)
sort_name_button.pack(side=tk.TOP, pady=5)

# Start checking for pending tasks
check_pending_tasks()

# Run the Tkinter event loop
root.mainloop()

