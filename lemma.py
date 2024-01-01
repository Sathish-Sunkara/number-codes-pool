#eulcid division lemma

a,b=list(map(int,input("enter the two numbers").split()))

def lemma(a,b):
    q=a//b
    r=a%b
    if r==0:
        print("the GCD is",b)
    else:
        lemma(b,r)
lemma(a,b)
        
    
