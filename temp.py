#n=int(input())
#str_=""
#while n!=0:
#   str_=str(n%2)+str_
#    n=n//2
#print('%08d'% int(str_))
    

n=int(input())
H=int(n//(2**7))
n=n%(2**7)
G=int(n//(2**6))
n=n%(2**6)
F=int(n//(2**5))
n=n%(2**5)
E=int(n//(2**4))
n=n%(2**4)
D=int(n//(2**3))
n=n%(2**3)
C=int(n//(2**2))
n=n%(2**2)
B=int(n//(2**1))
n=n%(2**1)
A=int(n//(2**0))
n=n%(2**0)
print(H,G,F,E,D,C,B,A)

Y=int(A*(2**0)+B*(2**1)+C*(2**2)+D*(2**3))
X=int(E*(2**0)+F*(2**1)+G*(2**2)+H*(2**3))
Dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
if X>=10:
    if Y>=10:
        print(Dic[X],Dic[Y])
    else:print(Dic[X],Y)
else:
    if Y>=10:
        print(X,Dic[Y])
    else:print(X,Y)
