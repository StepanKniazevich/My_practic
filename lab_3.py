from math import *
import random
i=0
arr = random.sample(range(-10, 10), 7)
spisok=random.sample(range(-10, 10), 7)
print("Вихідний список : ",arr)
Min=min(arr)
Max=max(arr)
print("Мінімальне значення у списку : " , Min )
print("Максимальне  значення у списку : " , Max )



while i<len(arr):
     spisok[i]=abs(arr[i])
     
     i=i+1


print("Cписок  за модулем :",spisok)

Min=min(spisok)
Max=max(spisok)
print("Мінімальне значення у списку по модулю: " , Min )
print("Максимальне  значення у списку по модулю: " , Max )

index_min = spisok.index(Min)
index_max = spisok.index(Max)
print("Індекс елемента з мінімальним значенням по модулю :" ,index_min)
print("Індекс елемента з максимальним значенням по модулю :" , index_max)


sub=1

if index_min>=index_max :
     while index_max<=index_min:
          sub*=arr[index_max]
          index_max+=1
else :
     while index_min<=index_min:
          sub*=arr[index_min]
          index_min+=1

          
print("Результат множення між максимальним і мінімальним значеннями :  ",sub)

