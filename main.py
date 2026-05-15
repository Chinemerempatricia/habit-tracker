from habit import Habit
from storage import save_habit, get_all_habits
from analytics import (
    get_daily_habits,
    get_weekly_habits,
    get_longest_streak
)
def menu():
    while True:
        print("=== HABIT TRACKER === ")
        print("1. Create Habit")
        print("2. View Habits")
        print("3. Complete Habit")
        print("4. Analyse Habit")
        print("5. Exit")
        choice = input("Choose option:")
        if choice == "1":
            name = input("Habit name:") 
            periodicity = input ("periodicity  (daily/weekly): ")
            habit = Habit(name, periodicity) 
            save_habit(habit)
            print("Habit created successfully!") 
        elif choice == "2":
            habits = get_all_habits()
            if not habits:
                print("No habits found.")
            for habits in habits:
                print(habits) 
        elif choice == "3":
            print("Habit completion recorded.")
        elif choice == "4":
            habits = get_all_habits()
            print("\nDaily Habites:")

        habits = get_all_habits()
        print(get_daily_habits(habits))
        print("\nWeekly Habits:")
        print(get_weekly_habits(habits))
        print("\nLongest Streak:")
        print(get_longest_streak(habits)) 

        print("Invalid Choice")

menu()
        
