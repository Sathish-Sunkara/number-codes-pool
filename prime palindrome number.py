"""
prime palindrome
number which satisfies both prime and palindrome
 """
def isprime(n):
    c=0
    for i in range(2,n):
        if n%i==0:
            c+=1
    if c==0:
        return True
    else:
        return False
def ispalindrome(n):
    if str(n)==(str(n))[::-1]:
        return True
    else:
        return False

n=int(input("enter the number"))
if ispalindrome(n) and isprime(n):
    print(n , "is a prime palindrome")
else:
    print(n , "is not a prime palindrome")

