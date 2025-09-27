def fancier_greet(name, day):
    print("Greetings, my good fellow " + name + "!")
    print("How are you doing this fine " + day + "?")

fancier_greet("Anders", "Thursday")
fancier_greet("Sandra", "Monday")


def sum_and_print(x, y):
    print(x + y)

a = 5
b = 10
sum_and_print(2 * b, b + a)

def another_greeting(name, day):
    greeting = "Hello, " + name + "! What a lovely " + day + "!"
    print(greeting)

name = "Martin"
day = "Wednesday"
another_greeting(name, day)

def silly_square(x):
    k = -x * x
    return k

a = 5
b = silly_square(a)
print(b)

def my_function(x, y):
    k = x + y
    if k > 10:
        return k
    return 0

print(my_function(3, 4))
print(my_function(30, 40))

def another_function(hours):
    if hours < 12:
        return "Good morning!"
    elif hours < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

print(another_function(15))

month = "December"
def new_year():
    month = "January"
new_year()
print(month)

def important_message():
    print("Attention!")
    print("Attention!")

def more_important_message():
    important_message()
    important_message()

more_important_message()

def sum_numbers(n):
    my_sum = 0
    for i in range(1, n + 1):
        my_sum = my_sum + i
        return my_sum

a = sum_numbers(3)
print(a)

def print_date(month, day):
    print("Month:", month, "Day:", day)

month = "January"
day = 31
