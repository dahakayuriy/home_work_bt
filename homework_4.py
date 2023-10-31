import random
# task1
random_number = random.randint(1, 10)
user = input("Guess the number from 1 to 10: ")
if user.isdigit():
    user = int(user)
    if 1 <= user <= 10:
        if user == random_number:
            print(f"Congratulations, you guessed the number {random_number}.")
        else:
            print(
                f"Unfortunately, you didn't guess the number, the correct number will be {random_number}.")
    else:
        print("Enter a number between 1 and 10.")
else:
    print("Enter a valid number from 1 to 10.")

# task 2
user_name = 'Yuriy'
user_age = 40
print(f"Hi, {user_name}, on your next birthday youll be {user_age+1} years!")

# task 3

input_string = input("Enter a string: ")

num_random_strings = 5

for _ in range(num_random_strings):
    random_string = ''.join(random.choice(input_string) for _ in input_string)
    print(random_string)
