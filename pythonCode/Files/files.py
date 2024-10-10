for i in range(2):
    f = open("file.txt","a")
    f.write("Hello")
    f.close()

f = open("file.txt","r")
print(f.read())
f.close()