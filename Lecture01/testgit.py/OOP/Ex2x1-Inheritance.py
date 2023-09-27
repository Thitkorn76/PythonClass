# class Pets:
#     dogs = []
#     def __init__(self, dogs):
#         self.dogs = dogs

#     class Dog:

#         specise = 'mammal'

#         def __init__(self, name, age):
#             self.name = name
#             self.age = age

#         def description(self):
#             return self.name, self.age
        
#         def speak(self, sound):
#             return "%s says %s" % (self.name, sound)
        
#         def eat(self):
#             self.is_hungry = False

# class RussellTerrier(Dog):
#     def run(self, speed):
#         return "%s runs %s" % (self.name, speed)
    
# class Bulldog(Dog):
#     def run(self, speed):
#         return "%s runs %s" % (self.name, speed)
    

# my_dogs = [
#     Bulldog("Tom", 6)
#     RussellTerrier("Fletcher", 7)
#     Dogs("Larry", 9)
# ]

# my_pets = Pets(my_dogs)


# print("I have {} dog.".format(len(my_pets.dogs)))
# for dog in my_pets.dogs:
#     print("{} is {}.".format(dog.name, dog.age))
# print("And they're all {}s, of course.".format(dog.species))