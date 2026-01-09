#Day 2: 30 Days of python programming
#Level 1
first_name = 'Raj'
last_name = 'Singh'
full_name = 'Raj Singh'
country_name = 'Mali'
city = 'Timbuktu'
age = 5
year = 2026
is_married = False 
is_true = False
is_light_on = False
vehicle, model, year_of_manufacture = 'Toyota', 'Corolla', 2020
#Level 2
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country_name))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(vehicle))
print(type(model))
print(type(year_of_manufacture))
print(len(first_name))
compare_length = len(first_name) > len(last_name)
print(compare_length)
total_length = len(first_name) + len(last_name)
print(total_length)

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
divide = num_one /num_two
mod = num_two % num_one
exp = num_two ** num_one
floor_division = num_one // num_two

#Circle calculations
r, pi = 30, 3.14
area_of_circle = pi * r**2
circum_of_circle = 2 * pi * r
print("Area of circle with radius ",r," is: ",area_of_circle)
r = print(input("Enter radius: "))
print("Area of circle: ",area_of_circle)
print("Circumference of circle: ",circum_of_circle)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country_name = input("Enter your country: ")
age = int(input("Enter your age: "))
print("Your name is ", first_name, last_name, ". You are ", age, " years old and live in ", country_name,".")