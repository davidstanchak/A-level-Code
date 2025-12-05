# dictionary = {
#     0:7,
#     1:40,
#     2:32,
#     3:19,
#     4:90,
#     5:40
# }

# items = [12,5,14,15,13,17,1,19]
# length = len(items)-1
# for i in range(length-1):
#     print(items)
#     for j in range(length-i):
#         if items[j+1] < items[j]:
#             prev = items[j]
#             items[j] = items[j+1]
#             items[j+1] = prev

# print(items)
def insertionSort():      
    items = [33, 4, 50, 18, 7, 45, 25, 39, 12, 29]
    length = len(items)
    for j in range(1,length):
        nextItem = items[j]
        i = j-1
        print(items)
        while i >= 0 and items[i] > nextItem:
            items[i+1] = items[i]
            i = i-1
            

        items[i+1] = nextItem
    return items
    


print(insertionSort())





    
