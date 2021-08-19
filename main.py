#from file import class
from animal import Animal
dog = Animal(name='Lizzy', age=3) #instance/object
cat = Animal(name='Zorka', age=10)
bird = Animal(name="Fufu", age=5)

print(dog.speak())
print(cat.speak())
print(bird.speak())

print(bird.intro())
#print(Animal.__dict__)
#You can use that to find out if you dont have access to the clas