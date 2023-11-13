#1
def favorite_movie(name_of_my_favorit_film):
    return name_of_my_favorit_film
name_of_my_favorit_film = "There will be blod"

print(f'My favorite movie is named: {favorite_movie(name_of_my_favorit_film)}')

#2
def make_country(country_name, capital):
    country_info = {country_name: capital}
    return country_info


ukraine_info = make_country('Ukraine', 'Kyiv')
print(ukraine_info)

#3
def make_operation(operator, *args):
    if operator == '+':
        return sum(args)
    elif operator == '-':
        return args[0] - sum(args[1:])
    elif operator == '*':
        result = 1
        for num in args:
            result *= num
        return result

print(make_operation('+', 7, 7, 2))        
print(make_operation('-', 5, 5, -10, -20)) 
print(make_operation('*', 7, 6))     