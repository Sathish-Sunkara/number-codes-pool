"""
twisted prime
if a number and its reversed form are both are the primes then it is atwisted prime
"""
def isprime(num):
    c=0
    for i in range(1,n+1):
        if num%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
    
n=int(input("enter the number"))

if((isprime(n)) and (isprime(int(str(n)[::-1])))):
    print(n , "is a twisted prime number")
else:
    print(n , "is not a twisted prime number")

    
