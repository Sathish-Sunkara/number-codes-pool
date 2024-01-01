"""
trimorphic number
cube of that number ends with the same number
"""
n=int(input("enter the number"))

if((str(n**3))[-1:-(len(str(n))+1):-1]==str(n)):
    print(n ,"is a trimorphic number")
else:
    print(n ,"is a not trimorphic number")
