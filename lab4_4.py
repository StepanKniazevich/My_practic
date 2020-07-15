mas='An independent and sovereign Ukraine is key to Euro Atlantic security. Redacted by Stepan'
Arr=[]                                                     
arr='aeiouyAEIOUY'
h=0
size=0
n=0
m=0
t=0
for i in range(len(mas)):
    for j in range(len(arr)):
     if mas[i]==arr[j] :
       Arr.append(mas[i])
      

print("Текст : ",mas)
print()
print("Усі голосні літери у тексті  : ",Arr )
