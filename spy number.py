#spy number
"""
sum of digits equals to product of digits
"""
def sum_of_digits(n):
    sum=0
    while(n>0):
        r=n%10
        n=n//10
        sum+=r
    return sum
n=int(input("enter the number"))
m=n
if (sum_of_digits(n**2)==m):
    print(m,"it is a neon number")
else:
    print(m,"it is not a neon number")



