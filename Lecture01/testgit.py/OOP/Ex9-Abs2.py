from abc import ABC, abstractmethod
class Absclass(ABC):
    def print(self,x):
        print("Passed value: ", x)
    @abstractmethod

    def task(self):
        print("we are inside Absclass task")

class test_class(Absclass):
    def task(self):
        print("We are inside test_class tsak")

class examle_class(Absclass):
    def task(self):
        print("we are insider example_class task")

test_obj = test_class()
test_obj.task()
test_obj.print(100)

examle_obj = examle_class()
examle_obj.task()
examle_obj.print(200)

print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
print("example_obj is istance of Absclass? ", isinstance(examle_obj, Absclass))