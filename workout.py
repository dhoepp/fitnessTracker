class Workout:
    def __init__(self, date, name):
        self.date = date
        self.name = name
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def summary(self):
        print(f"Workout: {self.name} on {self.date}")
        for e in self.exercises:
            print(f" - {e.name}")