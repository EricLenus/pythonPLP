#creating a class person
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

#creating a functin
    def introduce(self):
        print (f"hello, my name is {self.name}, I am {self.age} years old and I am {self.gender}")

#creating an instance 
person1 = Person("Eric", 18, "Male")

person1.introduce()