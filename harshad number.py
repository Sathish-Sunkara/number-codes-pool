"""
harshad number / niven number
sum of its digits divisible the number without rem
"""
def sum_digits(n1):
    sum1=0
    while(n1>0):
        rem=n1%10
        sum1+=rem
        n1=n1//10
    return sum1
        
n=int(input("enter the number"))

if n%sum_digits(n)==0:
    print(n ," is a niven number")
else:
    print(n ," is not a niven  number")
