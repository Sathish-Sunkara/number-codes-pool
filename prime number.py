#prime number


def is_prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return 1
    else:
        return 0

n=int(input("enter the number"))

flag=is_prime(n)

if(flag==1):
    print(n , "is a prime number")
else:
    print(n , "is not a prime number")
