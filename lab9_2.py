file=open("file.txt",'r')

data=file.readlines()

print("Завдання 5.2 а):")
for line in data:
  if line[0]=="Т":
    print(line[:-2])

print("\nЗавдання 5.2 б):")
for line in data:
  if len(line[:-2])>30:
    print(line[:-2])

print("\nЗавдання 5.2 в):")
for line in data:
  if line.count(' ')>3:
    print(line[:-2])

print("\nЗавдання 5.2 г):")
fragment=input("Введіть фрагмент рядка: ")

count_s=0
for line in data:
  if line[:-2].find(fragment)!=-1:
    print(line[:-2])
    count_s+=1
if count_s==0:
  print("Введений фрагмент: "+fragment+" відсутній у всіх рядках.\n")

file.close()