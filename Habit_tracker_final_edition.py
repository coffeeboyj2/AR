from tkinter import *

# Define a dictionary to store habits and their completion status
habits = {}

# Define a function to display the current status of all habits
def display_habits():
    habit_list.delete(0, END)
    for habit, status in habits.items():
        habit_list.insert(END, habit + " - " + ("Done" if status else "Not done"))

# Define a function to add a new habit
def add_habit():
    new_habit = habit_entry.get()
    if new_habit:
        habits[new_habit] = False
        habit_entry.delete(0, END)
        display_habits()

# Define a function to mark a habit as done
def mark_done():
    selected_habit = habit_list.get(ACTIVE).split(" - ")[0]
    habits[selected_habit] = True
    display_habits()

# Create the GUI
root = Tk()
root.title("Habit Tracker")

# Create the habit entry field and add button
habit_entry = Entry(root, width=50)
habit_entry.grid(row=0, column=0, padx=10, pady=10)
add_button = Button(root, text="Add Habit", command=add_habit)
add_button.grid(row=0, column=1, padx=10, pady=10)

# Create the habit listbox and mark done button
habit_list = Listbox(root, width=50)
habit_list.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
mark_done_button = Button(root, text="Mark Done", command=mark_done)
mark_done_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Display the initial habits
display_habits()

# Run the GUI
root.mainloop()