enter = int(input("what number should i count to??"))
for i in range(1,enter+1):
    file = open("file.txt", "a")
    file.write(str(i))
    file.close()

f = open("file.txt", "r")
print(f.read())
f.close()

