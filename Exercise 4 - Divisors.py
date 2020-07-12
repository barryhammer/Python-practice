#https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
#Exercise 4
divisor = int(input("Please enter a number between 1 and 100: "))
my_range = range(1, divisor)
for elem in my_range:
    if divisor % elem == 0:
        print(elem, end=",")