#1

def hello(name):
    return f"Hello, {name}!"

from homework_8 import hello

def greet_twice(name):
    greeting = hello(name)
    return f"{greeting} {greeting}"

from homework_8 import greet_twice

name = "Alice"
result = greet_twice(name)
print(result)

#2
import sys
print(sys.path)
import sys
sys.path.append("C:\Users\dahak\OneDrive\Рабочий стол\Python_Bogdan\p12")
print(sys.path)

#3

import mymod

mymod.test("C:\\Users\\dahak\\OneDrive\\Рабочий стол\\JS\\Plugins vs code.docx")