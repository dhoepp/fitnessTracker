class Exercise:
    def __init__(self, name, muscle_group):
        self.name = name
        self.muscle_group = muscle_group
        self.sets = []

    def add_set(self, reps, weight, time):
        self.sets.append({'reps': reps, 'weight': weight, 'time': time})