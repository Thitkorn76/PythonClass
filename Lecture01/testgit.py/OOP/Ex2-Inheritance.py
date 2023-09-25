class Dog:

    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{}is {} year old".format(self.name, self.age)
    
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
    
class RusssellTrerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
    
jim = Bulldog('jim', 12)
print(jim.description)

print(jim.run("slowly"))

print(isinstance(jim,Dog))

julie = Dog('julie', 100)
print(isinstance(julie, Dog))

johnnywalker = RusssellTrerrier("Johnny Walker", 4)
print(isinstance(johnnywalker, Bulldog))

print(isinstance(julie, jim))

