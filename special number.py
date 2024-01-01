"""
special number
 sum of the factorials of the digits equals to that number
 """

n=int(input("enter the number"))

m=n
sum1=0
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact
sum1=0
while(n>0):
    rem=n%10
    fact_rem=factorial(rem)
    sum1=sum1+fact_rem
    n=n//10
if sum1==m:
    print(m ," is a special number")
else:
    print(m ," is not a special number")



