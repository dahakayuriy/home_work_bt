import random

#1
random_numbers = [1, 7, 65, 3, 8, 23, 44, 48, 51]
print(max(random_numbers))

random_numbers = []

count = 0
while count < 10:
    random_numbers.append(random.randint(1, 100))
    count += 1

max_number = random_numbers[0]
i = 1
while i < len(random_numbers):
    if random_numbers[i] > max_number:
        max_number = random_numbers[i]
    i += 1

print("List of random numbers:", random_numbers)
print("The largest number of:", max_number)

#2
list1 = []
list2 = []

count = 0
while count < 10:
    list1.append(random.randint(1, 10))
    list2.append(random.randint(1, 10))
    count += 1
print(list1)
print(list2)

list3 = []
i = 0
while i < len(list1):
    number = list1[i]
    if number in list2 and number not in list3:
        list3.append(number)
    i += 1
print(list3)

#3

# list1_100 = []
# count = 1
# while count <= 100:
#     list1_100.append(count)
#     count += 1
# print(list1_100)
list1_100 = list(range(1, 100))

divisible_by_7 = []
i = 0
while i < len(list1_100):
    if list1_100[i] % 7 == 0 and list1_100[i] % 5 != 0:
        divisible_by_7.append(list1_100[i])
    i += 1
print(divisible_by_7)
