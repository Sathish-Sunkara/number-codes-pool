"""
happy number
recursively check sum of the digits squares is 1
"""

def sum_digit_powers(num):
    sum1=0
    while(num>0):
        rem=num%10
        sum1=sum1+rem**2
        num=num//10
    print(sum1)
    return sum1


n=int(input("enter the number"))
m=n

while(True):
    a=sum_digit_powers(n)
    if a==1:
        print(m , "is a happy number")
        break
    elif len(str(a))==1:
        print(m , "is not a happy number")
        break
    else:
        n=a
        
