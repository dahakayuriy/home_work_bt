# task1
string_of_letters = 'python'

if len(string_of_letters) >= 2:
    print(string_of_letters[0] + string_of_letters[1] +
          string_of_letters[-2] + string_of_letters[-1])
elif len(string_of_letters) < 2:
    print('empty string')

# task2
phone_number = '0834563810'

if phone_number.isdigit() and len(phone_number) == 10:
    print("Everything is ok, the number is entered correctly")
else:
    print("This is wrong number")

# task3
math_expression = "2 + 2"
expected_answer = eval(math_expression)
user_answer = int(input(f"Solve the expression {math_expression}: "))
if user_answer == expected_answer:
    print("Right! Your answer is correct.")
else:
    print(f"Wrong. Correct answer: {expected_answer}")

# task 4
user_name = 'Yuriy'
saved_name = user_name.lower()
if user_name.lower() == saved_name:
    print("True")
else:
    print("False")
