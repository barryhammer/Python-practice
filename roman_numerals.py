import ctypes

my_input = input("Please enter a roman numeral: ")

'''
This was my attempt at converting Roman Numerals. There were two problems:
    1) Although I could iter through the list, it kept adding the next value, even if it shouldn't have (EG. MMCM = 3100 instead of 2900)
    2) I knew that my code should be much shorter for what this is.
In the end, I realized I was spending way too much time trying to re-invent the wheel.
This code I'm leaving here for my own use, as part of my learning process.

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
'''

'''
This code I found at https://www.oreilly.com/library/view/python-cookbook/0596001673/ch03s24.html
I just removed the exception errors, since I didn't think they were necessary for this exercize.
'''
nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
sum = 0
for i in range(len(my_input)):
        value = nums[my_input[i]]
        # If the next place holds a larger number, this value is negative
        if i+1 < len(my_input) and nums[my_input[i+1]] > value:
            sum -= value
        else: sum += value

ctypes.windll.user32.MessageBoxW(0, "Your Roman Numeral {} equals {}.".format(my_input, sum), "Roman Numeral Converter", 1)
# Found this at https://stackoverflow.com/questions/2963263/how-can-i-create-a-simple-message-box-in-python

'''
In the end, there were a few lessons learned:
    1) If it's taking too long to find the solution, you need to get the help of someone else who can point you in the right direction
    2) Although I did learn about dictionaries, I didn't think to use them. They make this solution much more elegant.
    3) I was wracking my brains trying to get nums[my_input[i+1]] properly. Hopefully now that I have this solution at hand, I'll be able
        to reference it again in the future.
'''
