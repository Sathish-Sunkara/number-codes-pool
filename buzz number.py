#buzz number program
#it is divisible by seven or ends with seven

def is_buzz(n):
    if( (n%10==7) or (n%7==0)):
        return 1
    else:
        return 0

n=int(input("entr the number"))
flag=is_buzz(n)
if(flag==1):
    print(n , "is a buzz number")
else:
    print(n , "is not a buzz number")
