#https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
#Exercise 5
#https://www.tutorialspoint.com/generating-random-number-list-in-python
#Answer for set found in comments.
import random

a = random.sample(range(1, 100), 10)
b = random.sample(range(1, 100), 13)
print(list(set([x for x in b if x in a])))
print(a)
print(b)