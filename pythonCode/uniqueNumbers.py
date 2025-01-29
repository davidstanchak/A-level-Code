numbers = [4,5,6,4,7,8,5]
unique = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            unique.append(numbers[i])