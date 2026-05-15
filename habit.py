from datetime import datetime
class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity
        self.created_at = datetime.now().strftime("%Y-%m-%d- %H: %M: %S")
        
        self.completions = []
    def check_off(self):
        completion_time = datetime.now().strftime("%Y-%m-%d %H: %M: %S")
        self.completions.append (completion_time) 

    def get_streak(self):
        return len(self.completions)
    def to_dict(self):
        return {
            "name":self.name,
            "periodicity": self.periodicity,
            "created_at": self.created_at,
            "completions": self.completions
        }
    def __str__(self):
        return f"{self.name} ({self.periodicity})"


        
        