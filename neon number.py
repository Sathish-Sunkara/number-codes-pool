#neon number
"""
A neon number is a number where the sum of digits of square of the number is equal to the number.
The task is to check and print neon numbers in a range. Examples: Input : 9 Output : Neon Number Explanation:
square is 9*9 = 81 and sum of the digits of the square is 9
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



