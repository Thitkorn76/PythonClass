class Dog:
    species = 'mammal'

    def calAge(self,age):
        print('Dog Age is {}'.format(age*3))

class SomeBread(Dog):
    pass

class SomeOTherBread(Dog):
    species = 'reptile'
    def calAge(self, age):
        print('Dog Age is {}'.format(age*4))

    
frank = SomeBread()
print(frank.species)
frank.calAge

beans = SomeOTherBread()
print(beans.species)
print(beans.calAge)

