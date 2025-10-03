odd_digits = [1, 3, 5, 7, 9]
print(odd_digits)

even_digits = [0, 2, 4, 6, 8]
print(even_digits)

common_allergies = ['peanuts', 'shellfish', 'dairy', 'eggs', 'gluten']
print(common_allergies)

noble_gasses = ['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
print(noble_gasses)

mixed_list = [1, 'hello', 3.14, True]
print(mixed_list)

numpad_buttons = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [0]]
print(numpad_buttons)

i_am_empty_inside = []
print(i_am_empty_inside)

list_of_numbers = [10, 20, 30, 40, 50]
print("item at index 0:", list_of_numbers[0])
print("item at index 3:", list_of_numbers[3])

noble_gasses = ['helium', 'neon', 'argon', 'krypton', 'xenon', 'radon']
print("item at index 1:", noble_gasses[1])
print("item at index -1:", noble_gasses[-1])
print("item at index -2:", noble_gasses[-2])
print("item at index -3:", noble_gasses[-3])

my_list = ["Zero", "One", "Two", "Three", "Four", 
           "Five", "Six", "Seven", "Eight", "Nine"]
print(my_list[2:5])
print(my_list[3:8:2])
print(my_list[0:10:3]) # the last number basically means "step"

my_list = ["Zero", "One", "Two", "Three", "Four", 
           "Five", "Six", "Seven", "Eight", "Nine"]
print(my_list[::2])
print(my_list[:-1])
print(my_list[::-1])
print(my_list[3:])
print(my_list[:2])

my_list = ["Zero", "One", "Two", "Three", "Four", 
           "Five", "Six", "Seven", "Eight", "Nine"]
second_list = my_list[3:8]
print(second_list)

my_list = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
my_list[0] = 'one'
print(my_list)
my_list[-1] = 'fem'
print(my_list)

this_list = ["apple", "banana", "cherry"]
this_list[3:] = ["blackcurrant", "watermelon"]
print(this_list)
this_list[1:3] = []
print(this_list)

digits = [3, 117, 4, -1.9, 5, 9.8, 0]
print("Length of digits:", len(digits))
print("Sum of digits:", sum(digits))
print("Minimum of digits:", min(digits))
print("Maximum of digits:", max(digits))


print("Any:", any(digits))
print("All:", all(digits))

test_1 = 'Anna' == 'Anna'
test_2 = 'Anna' == 'anna'
test_3 = 'Anna' == 'ANNA'
test_4 = 'Anna' == 'Anne'

all_tests = [test_1, test_2, test_3, test_4]
print('All tests:', all(all_tests))
print('Any tests:', any(all_tests))

list1 = ['water', 'earth']
list2 = ['fire', 'air']
elements = list1 + list2
print(elements)
elements = elements + list2
print(elements)
elements = elements + 4 * list1
print(elements)

spam_list = ["SPAM"] * 5
print(spam_list)
the_best_number = [216] * 7
print(the_best_number)
concat_list = spam_list + the_best_number
print(concat_list)

my_list = [3, 1, 4, 1, 5, 9, 2]
print(my_list)
my_list.sort()
print(my_list)

my_list = [3, 1, 4, 1, 5, 9, 2]
print(my_list)
my_list.sort(reverse=True)
print(my_list)

my_list = ["A", "B"]
my_list.append("C")
print(my_list)

models = ['linear', 'quadratic', 'power', 'exponential']
models.pop(1)
print(models)
models.pop(1)
print(models)

my_list = ["A", "B"]
my_list.extend(["C", "D"])
print(my_list)

my_list = ["A", "B"]
my_list.extend(["C", "D"])
print(my_list)

names = ["Clara", "Alice", "Bob", "David", "Anna", "Eve", "Elvis", "Aaron"]
names.sort()
print(names)

my_list = ["A", "B", "A", "C", "a"]
print(my_list.count("A"))

my_list = ["A", "B", "C", "A"]
print(my_list.index("A"))
print(my_list.index("C"))

a = ['one', 'two', 'three']
b = a
print(a)
b[1] = '2'
print(a)

a = ['one', 'two', 'three']
b = a
a.append('four')
print(b)

a = ['one', 'two', 'three']
b = a.copy()
a.append('four')
print(b)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for i in range(len(weekdays)):
    print('Hello ' + weekdays[i])

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for weekday in weekdays:
    print('Hello ' + weekday)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
lengths = []
for weekday in weekdays:
    lengths.append(len(weekday))
    if weekday == "Monday":
        print("I hate Mondays...")
    else:
        print("I like", weekday + "s")
print(lengths)

distances = [12.8, 10.7, 6.6, 9.9, -0.2, 5.5, -0.3, 14.7]
for i in range(len(distances)):
    if distances[i] < 0:
        distances[i] = 0.0
print(distances)

recorded_data = [3.0, 4.2, -1, -1, 2.5, 3.7, -1000]
positive_data = []
for value in recorded_data:
    if value > 0:
        positive_data.append(value)
print(positive_data)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
temperatures = [20, 21, 17, 22, 24]
for i in range(len(weekdays)):
    print(weekdays[i] + ":", temperatures[i], "degrees")

vowel_string = "aeiou"
vowels = list(vowel_string)
print(vowels)

numbers_range = range(20)
numbers = list(numbers_range)
print(numbers)

def modify_list(my_list):
    my_list.append("banana")

fruits = ["apple", "orange"]
modify_list(fruits)
print(fruits)

def modify_list(my_list):
    my_list.append("banana")

fruits = ["apple", "orange"]
modify_list(fruits)
print(fruits)
#
some_list = [1, 2, 3]
print(5 in some_list)
print(1 in some_list)

condition = 13 in [1, 2, 3, 4, 5]
print(condition)

vowels = ['a', 'e', 'i', 'o', 'u', "y"]
print('y' in vowels)

for energy_source in ['wind', 'coal']:
    if energy_source in ['solar', 'wind', 'hydropower', 'geothermal', 'biomass']:
        print(energy_source, "is a renewable energy source.")
    else:
        print(energy_source, "is not a renewable energy source.")
#
cat_family = ['lion', 'tiger', 'leopard', 'cheetah']
animal = 'bear'
if animal not in cat_family:
    print(animal + " is not in the cat family.")

common_allergies = ['peanuts', 'shellfish', 'dairy', 'eggs', 'gluten']
common_allergies = common_allergies.append('soy')
print(common_allergies)

danish_vowels = ['a', 'e', 'i', 'o', 'u', 'y']
english_vowels = danish_vowels[:-1]
danish_only_vowels = danish_vowels[5:5]
print(english_vowels)
print(danish_only_vowels)

afternoon_activities = ['study', 'work', 'exercise', 'relax']
afternoon_activities.extend('sleep') #the difference between append and extend is that append adds the entire argument as a single element to the list, while extend adds each element of the argument to the list
print(afternoon_activities)

# list = ['x_ray', 'mri', 'ct_scan']
# numbers = list(range(1, 6))
imaging_list = ['x_ray', 'mri', 'ct_scan']
numbers = list(range(1, 6))

my_favorite_functions = ['max', 'min', 'sum', 'len']
print("The length of a list can be estimated with", my_favorite_functions[3])

spooky_electronics = ['resistor', 'capacitor', 'inductor', 'transistor', 'diode']
spooky_electronics.pop(0)



my_list = list(range(1,4)) * 3
print (my_list)

materials = ['concrete', 'steel', 'wood', 'glass', 'aluminum']
count = 0
for material in materials:
    if len(material) > 5: #checks if the length of each material is greater than 5
        count = count + 1
print(count)