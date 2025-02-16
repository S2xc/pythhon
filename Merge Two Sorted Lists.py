list1 = [1,2,4]
list2 = [1,3,4]

#list1[1:1] = list2

for i in range(len(list1)):
    for j in range((len(list1)-i-1)):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
            
print(list1)
    













# Refactored function for better performance 2025-02-16 14:42:31
