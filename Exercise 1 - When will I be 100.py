#https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
#Exercise 1
from datetime import datetime

dateyear = datetime.now().year

your_year = int(input("Please enter your current age: "))
no_input = int(input("Enter number of times you want it printed: "))
one_hundred = 100 - your_year + dateyear

for i in range(no_input):
    print("You will be 100 years old in the year", one_hundred, "\n")
