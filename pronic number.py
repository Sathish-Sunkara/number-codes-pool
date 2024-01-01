"""
pronic number

 if N is said to be a pronic then the product of the consecutive numbers in the range of (1,n) is equals to n
 """
n=int(input("enter the number"))
flag=0
for i in range(1,n):
    if i*(i+1)==n:
        flag=1
        print(n , "is a pronic number")
if flag==0:
        print(n , "is not a pronic number")

