class Animal:
   def __init__(self, name, age): #initialize when we feed into IV
       #instance variable
       self.name = name
       self.age = age
    #instance method
   def speak(self):
        return f"My name is {self.name} and I am {self.age} years old"

   def intro(self):
          return f"I am {self.name}"