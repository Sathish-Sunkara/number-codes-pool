"""
trimorphic number
cube of that number ends with the same number
"""
n=100
while(True):
    if((str(n**3))[-1:-(len(str(n))+1):-1]==str(n)):
        print(n ,"is a trimorphic number")
    n+=1

