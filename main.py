from workout import Workout
from exercise import Exercise
from calculations import Calculations


def main():
    print("Welcome to Fitness Tracker!")
    print("This is your first Python project kickoff")  

    w = Workout("2025-10-22", "Push Day")
    chest_press = Exercise("Chest Press", "Chest")
    chest_press.add_set(8,55,30)
    w.add_exercise(chest_press)
    w.summary()
    orm = Calculations()
    setOrm = orm.calc1RM(chest_press.sets[0]['reps'],chest_press.sets[0]['weight'])
    print(f"1RM is  {round(setOrm, 1)}")
    


if __name__ == "__main__":
    main()