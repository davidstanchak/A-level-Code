arr = [44,12,83,11,900,1]
n = len(arr)-1

for i in range(n):
    for j in range(n-i):
        if arr[j] > arr[j+1]:
            prev = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = prev
            
print(arr)
