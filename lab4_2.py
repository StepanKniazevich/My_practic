from array import array
arr=['князевич_князь','степан','іванович']
mas=[]
p=0
r=0

print("Вихідні слова:  ",arr)
 
for k in range(len(arr[r])):
        for i in [1,2]:     
            for j in range(len(arr[i])):
             
             if arr[r][k]==arr[i][j]:
                p=p+1
               
                
        if p==0:
         
         mas.append(arr[r][k])
        
         p=0  
        else: p=0         
    
        
            
print("Букви , які не повторються у інших словах: ",mas)               
               
