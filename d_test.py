
def bubl(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)


bubl(arr=[2,3,4,5,6,7,1])





# Refactored function for better performance 2025-02-16 14:46:07

# Refactored function for better performance 2025-02-16 14:51:29

# Refactored function for better performance 2025-02-16 14:52:00
