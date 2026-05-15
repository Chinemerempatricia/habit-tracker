from habit import Habit
def test_habit_creation(): 
    habit = Habit("Exercise", "daily")

    assert habit.name == "Exercise"
    assert habit.periodicity == "daily"

def test_check_off():
    habit = Habit("Read", "dairly") 
    habit.check_off() 
    assert len(habit.completions) == 1


