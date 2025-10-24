class Calculations:
    def __init__(self):
         self.ORM = []
         
         
    def calc1RM(self, reps, weight):
         self.ORM.append({'reps': reps, 'weight': weight})
         c = weight * (1 + reps/30)
         return c
    

mycalc = Calculations()

print(mycalc.calc1RM(8,50))