from math import sqrt
c=int(input('Enter a value :'))
y=sqrt(c)
x=y
z=y-int(x)
if z==0:
    print(c,'is a perfect square')
else:
    print(c,'is not a perfect square')
