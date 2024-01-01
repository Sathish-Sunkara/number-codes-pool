#strong number
"""sum of the digits factorials is equals to that number"""

def factorial(rem):
    s=1
    for i in range(1,rem+1):
        s=s*i
    return s
        

def is_strong(n):
    m=n
    s=0
    while(n>0):
        r=n%10
        s=s+(factorial(r))
        n=n//10
    if s==m:
        return 1
    else:
        return 0

    
n=int(input("enter the number"))

flag=is_strong(n)

if(flag==1):
    print(n , "is a strong number")
else:
    print(n , "is not a strong number")


