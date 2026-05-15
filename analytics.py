from functools import reduce
def get_all_habits(habites):
    return habites
def get_daily_habits(habits):
    return list( 
        filter
        (lambda habit: habit["periodicity"] == "daily", habits)

    )

def get_weekly_habits(habits):
    return list( 
        filter(
            lambda habit: habit["periodicity"] == "weekly", 
 habits


        )

    )
def get_longest_streak(habits): streaks = list(
            map(
                lambda habit: len(habit ["completions"]), habits
 
            )
) 
