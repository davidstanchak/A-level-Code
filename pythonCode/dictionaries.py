# key value pairs

person1 = {
    "Name" : "David",
    "Age": 16,
    "DOB": "12th September"
}

print(person1["Age"])

for key in person1:
    print(key, person1[key])
    

numbers = [1,2,12,13,22]

for i in range(len(numbers)):
    print(i, numbers[i])