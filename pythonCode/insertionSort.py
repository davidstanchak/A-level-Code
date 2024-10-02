import random
import json
numbers = [random.randint(1,1000) for _ in range(1000)]

with open("unsorted_numbers.json", "w") as f:
    json.dump(numbers, f)
    
def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

            arr[j+1] = key
    return arr

with open("sorted_numbers.json", "w") as f:
    json.dump(insertion_sort(numbers), f)
