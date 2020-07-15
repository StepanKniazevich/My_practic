from math import *
a=4.5
Res=0
while True:
    if a <= 16.4:
        x=a
        Res=pow(cos(x),2)/(pow(x,2)+1)

        print("Результат при x = ",x," :  ", Res)
    else:
        break

    
    a=a+2.2
