#Code 6.3: Your Name

#Define a list containing your first, last, and any middle names. For example:

#my_name = ["Lars", "Løkke", "Rasmussen"]
#Now, print out a message like this, but for your name, using the list you defined:

#My first name is Lars and my last name is Rasmussen
#In total, I have 3 names.

#Ensure that your message works for other names, with a varying number of middle names. Test with the my_name defined above and with a person who has no middle name.

my_name = ["Lars", "Løkke", "Rasmussen"]

first_name = my_name[0]
last_name = my_name[-1]
num_names = len(my_name)

print(f"My first name is {first_name} and my last name is {last_name}")
print(f"In total, I have {num_names} names.")
