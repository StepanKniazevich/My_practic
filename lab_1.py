from math import *
x=9
a=0.3*log10(exp(-x))
b=(atan(x)- pow(sin(x),2))/(4*sqrt(log(abs(x-1))))
u=a*b
print("Result:  " ,u )

