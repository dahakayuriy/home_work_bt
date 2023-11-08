#1
sentence = "cats were running around the room"
word_count = {}
for word in sentence.split():
    word = word.strip('.,!?"\'()[]{};:')
    if word not in word_count:
            word_count[word] = 1
    else:
            word_count[word] += 1

print(word_count)

#2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_prices = {}

for product, quantity in stock.items():
    if product in prices:
        price_per_unit = prices[product]
        total_price = quantity * price_per_unit
        total_prices[product] = total_price

print(total_prices)

# 3
tuple_list = []

for i in range(1, 11):
    j = i ** 2
    tuple_list.append((i, j))

print(tuple_list)

# 4
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_to_numbers = dict(enumerate(days_of_week, start=1))
numbers_to_days = {day: number for number, day in days_to_numbers.items()}

print(days_to_numbers)
print(numbers_to_days)