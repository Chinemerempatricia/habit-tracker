import json
import os
FILE_NAME = "habit.json"
def load_habits():
    if not os.path.exists(FILE_NAME): 
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file) 
def save_habit(habit):
    habits = load_habits()

    habits.append(habit.to_dict())

    with open(FILE_NAME, "w") as file:
        json.dump(habits, file, indent=4)
def get_all_habits():
    return load_habits()