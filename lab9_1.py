def sort_data(data, _file):
  list_d = list(data.items())
  list_d.sort(key=lambda i: i[1], reverse=True)
  for i in list_d:
    print(i[0], ':', i[1])
    _file.write(i[0]+" "+i[1]+"\n")

def add_students(name,surname,grid,_file):
  _file.write(surname+" "+name+" "+str(grid))

students_file=open("students.txt",'rt+')

students_data=students_file.read()

dict={}
i=0
for word in students_data.split():
  if i%3==0:
    key_d=word
    key_d+=" "
  elif i%3==1:
    key_d+=word
  elif i%3==2:
    dict.update({key_d:word})
  i+=1

students_file.close()

stud_for_sort=open("students.txt",'w')
sort_data(dict, stud_for_sort) #сортування у файлі
stud_for_sort.close()

stud_file=open("students.txt",'a+')
add_students("Степан","Князевич",4.8,stud_file)
stud_file.close()
