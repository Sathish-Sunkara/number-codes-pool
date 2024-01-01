"""
super digit
sum of the digits og the number until it reaches the single digit
"""
n=int(input("enter the number"))
m=n
while(n>=10):
    x=n
    sum=0
    while(x>0):
        r=x%10
        sum+=r
        x//=10
    n=sum
print("the super digit of {} is {}".format(m,n))
