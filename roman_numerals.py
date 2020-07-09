import ctypes

my_input = input("Please enter a roman numeral: ")

# Split value into individual characters that can be iterated
def split(word):
    return list(word)
my_list = split(my_input)

# Starting value for number
my_num = 0

# Iterate through list
for i in my_list:
    if i == 'M':
        my_num += 1000
    elif i == 'D':
        my_num += 500
    elif i == 'C':
        # Check if next character is M, in which case CM = 900
        for j in my_list[1:2]:
            if j == 'M':
                my_num += 900
            else:
                my_num += 100
    elif i == 'L':
        my_num += 50
    elif i == 'X':
        # Check if next character is M, in which case XM = 990; if next character is C CM = 90
        for j in my_list[1:2]:
            if j == 'M':
                my_num += 990
            elif j == 'C':
                my_num += 90
            else:
                my_num += 10
    elif i == 'V':
        my_num += 5
    elif i == 'I':
        # Check if next character is another Roman Numeral, in which case my_num += value -1
        for j in my_list[1:2]:
            if j == 'M':
                my_num += 999
            elif j == 'D':
                my_num += 499
            elif j == 'C':
                my_num += 99
            elif j == 'L':
                my_num += 49
            elif j == 'X':
                my_num += 9
            elif j == 'V':
                my_num += 4
            else:
                my_num += 1
    else:
        my_num += 0

ctypes.windll.user32.MessageBoxW(0, "Your Roman Numeral {} equals {}.".format(my_input, my_num), "Roman Numeral Converter", 1)
# Found this at https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python
