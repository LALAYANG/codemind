arr = [3, 100, 4, 5, 150, 6]
n = len(arr)
mpis = arr[:]
for i in range(n):
    current_prod = arr[i]
    j = i + 1
    while j < n:
        if arr[j-1] > arr[j]: 
            break
        current_prod *= arr[j]
        if current_prod > mpis[j]:
            mpis[j] = current_prod 
        j = j + 1
print(max(mpis))