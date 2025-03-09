#polynomial: x-(1-x^2/2+x^4/24)

def Polynomial(x):
    return x-1+ (x**2) /2 - (x**4) /24

def Derivative(x):
    return 1+x-(x**3)/6

#iteration for Newton's Method:
count = 0
sol=1

while count<50:
    sol=sol - Polynomial(sol)/Derivative(sol)
    count +=1

print(sol)