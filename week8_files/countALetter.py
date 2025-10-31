def count_letter(filename, letter):

    file = open(filename, 'r')
    content = file.read()
    file.close()
    
    letter = letter.lower()
    
    count = 0
    
    for character in content:
        if character.lower() == letter:
            count = count + 1
    
    return count

filename = "week8_files/weeksFiles/quick_fox.txt"
letter = 'a'

file = open(filename, 'r')
content = file.read()
file.close()
print("Length of file:", len(content))

result = count_letter(filename, letter)
print("The letter", letter, "appears", result, "times")