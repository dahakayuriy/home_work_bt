#1
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.first_name} {self.last_name} and I am {self.age} years old.")


person = Person("Carl", "Johnson", 26)

person.talk()

#2
class Dog:
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        equivalent_age = self.dog_age * self.age_factor
        return equivalent_age

dog1 = Dog(3)
print(f"The dog's age in human equivalent is: {dog1.human_age()} years")