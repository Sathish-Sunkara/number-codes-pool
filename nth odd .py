#getting nth odd number without even digits in it 

n = int(input("enter the number"))

ans= 0
while(n>0):
    if n%5 == 1:
        ans = ans*10+1
        n = n//5
    elif n%5 == 2:
        ans = ans*10 + 3     #here the for every remainder there are unique values  .  
        
        n = n//5
    elif n% 5 == 3:
        ans = ans*10 + 5
        n = n//5
    elif n% 5 == 4:
        ans = ans*10 + 7
        n = n//5
    else:
        ans =  ans*10 + 9    #according to remainder values(9) are placed at ans this ans will reversed then we get the nth odd number
        n = n//5
        n-=1   #for avoiding zero remainder next time
print(str(ans)[::-1])
        
    
