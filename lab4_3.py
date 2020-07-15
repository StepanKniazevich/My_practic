mas='An independent and sovereign Ukraine is key to Euro Atlantic security'
arr='aeiouyAEIOUY'

size=0
n=0
m=0
t=0
for i in range(len(mas)):
    if mas[i]==' ':
        t+=1
    for j in range(len(arr)):
     if mas[i]==arr[j] :
      n+=1

size=len(mas)-t

b=size-n

print("Кількість букв у тексті : ",size )
print("Кількість проголосних ", b)
print("Кількість голосних",n)

if b>n:
         print("Приголосних більше")
else:
    print("Голосних більше")

