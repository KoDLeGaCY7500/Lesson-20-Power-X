def flips(n1,n2):
    flip=0
    while (n1>0 or n2>0):
        t1=n1&1
        t2=n2&1
        if t1 != t2:
            flip+=1
        n1>>=1
        n2>>=1
    return flip
n1=int(input("Enter 1st number: "))
n2=int(input("Enter 2nd number: "))
print("Number of flips needed: ",flips(n1,n2))