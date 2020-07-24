lst1 = []
n = int(input("Enter number of elements : ")) 

for i in range(0, n): 
    ele = int(input()) 
    lst1.append(ele)  
print(lst1) 

for num in lst1: 

    if num >= 0: 
        print(num, end = " ") 
 
lst2 = [] 

n = int(input("\nEnter number of elements : ")) 

for i in range(0, n): 
    ele = int(input()) 
    lst2.append(ele)  
print(lst2) 

for num in lst2: 

    if num >= 0: 
        print(num, end = " ") 
