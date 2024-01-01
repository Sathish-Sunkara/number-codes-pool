"""
sunny number
the number n is sunny when n+1 is aperfect square

"""
from math import sqrt

n=int(input("enter the number"))
if(int(sqrt(n+1))==sqrt(n+1)):
    print(n , "is a sunny number")
else:
    print(n , "is not a sunny number")


