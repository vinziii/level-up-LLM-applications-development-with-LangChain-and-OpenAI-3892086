class AIAgent:
   def __init__(self, name, model):
       self.name = name
       self.model = model
       self.status = "idle"
   def introduce(self):
       print(f"I am {self.name}, running on the {self.model} model.")
   def activate(self):
       self.status = "active"
       print(f"{self.name} is now {self.status}!")
   def shutdown(self):
       self.status = "inactive"
       print(f"{self.name} is now {self.status}.")

       if self.status == "inactive":
           print(f"Charging {self.name}...")
           print(".......")
           self.status = "active"
           print(f"{agent1.name} is now active!")
       
   def get_status(self):
       return self.status
   

class FitnessTracker:
   def __init__(self,name,action=None,workout=None):
      self.name = name
      self.workouts=["Running", "Cycling", "Swimming"]
      self.action = action

   def add_workout(self, workout):
      self.workouts.append(workout)
      print(f"{workout} added to workouts.")

   def remove_workout(self, workout):
      if workout in self.workouts:
          self.workouts.remove(workout)
          print(f"{workout} removed from workouts.")
      else:
          print(f"{workout} not found in workouts.")



if __name__ == "__main__":

    # Tracker = FitnessTracker("Vindya", "add", "Yoga")
    Tracker = FitnessTracker("Vindya")

    if Tracker.action == "add":
        Tracker.add_workout("Yoga")

    elif Tracker.action == "remove":
        Tracker.remove_workout("Yoga")

    else:
        print("No change in workouts.")