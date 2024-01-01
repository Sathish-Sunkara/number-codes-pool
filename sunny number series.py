"""
sunny number
the number n is sunny when n+1 is aperfect square

"""
from math import sqrt

n=1
while(True):
    if(int(sqrt(n+1))==sqrt(n+1)):
        print(n , "is a sunny number")
    n+=1
    if n==10000:
        break


