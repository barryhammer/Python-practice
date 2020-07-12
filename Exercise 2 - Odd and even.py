#https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
#Exercise 2
user_no = int(input("Please enter a number: "))

if user_no % 2 == 0:
    if user_no % 4 == 0:
        print("Your number is divisible by 4.")
    else:
        print("Your number is an even number.")
else:
    print("Your number is an odd number.")
