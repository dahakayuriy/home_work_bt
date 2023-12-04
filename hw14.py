#1
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying hard.")

class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def get_salary(self):
        print(f"{self.name}'s salary is ${self.salary}.")

person1 = Person("John", 30)
person1.introduce()

student1 = Student("Alice", 16, 11)
student1.introduce()
student1.study()

teacher1 = Teacher("Mr. Smith", 40, "Math", 50000)
teacher1.introduce()
teacher1.teach()
teacher1.get_salary()


#4
class CustomException(Exception):
    def __init__(self, msg):
    
        super().__init__(msg)

        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Error: {msg}\n")

try:
    raise CustomException("This is a custom exception")
except CustomException as ce:
    print(f"Caught CustomException: {ce}")

# My example
class Animal:
    def __init__(self):
        self.limbs = 4
        self.eyes = 2

    def display_info(self):
        print(f"Limbs: {self.limbs} Eyes: {self.eyes}")


class FlyingAnimal(Animal):
    # eyes = None

    def __init__(self):
        super().__init__()
        self.can_fly = True

    def display_info(self):
        super().display_info()
        print("This type can also fly.")

    # def display_info(self):
    #     print(f"Limbs: {self.limbs}")
    #     print("This type can also fly.")


class SixEyesAnimal(FlyingAnimal):
    def __init__(self):
        super().__init__()
        self.eyes = 6

    def display_info(self):
        super().display_info()
        print("Extra: 6 eyes.")


animal = Animal()
flying_animal = FlyingAnimal()
six_eyes_animal = SixEyesAnimal()

print("Animal:")
animal.display_info()

print("\nFlying Animal:")
flying_animal.display_info()

print("\nSix Eyes Animal:")
six_eyes_animal.display_info()