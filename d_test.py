
def bubl(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(arr)


bubl(arr=[2,3,4,5,6,7,1])




