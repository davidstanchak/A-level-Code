my_list = [6,3,7,0,1,4]

def list_split(items):

    if len(items) <= 1:
        return items
    midpoint = (len(items) - 1)//2
    left_list = items[:midpoint+1]
    right_list = items[midpoint+1:len(items)]

    left_list = list_split(left_list)
    right_list = list_split(right_list)

    # mergedList = merge_sort(left_list,right_list)
    merged_items = merge_sort(left_list,right_list)

    return merged_items

print(list_split(my_list))

# print(list_split(my_List))
def merge_sort(left,right):

    merged = [] 
    index_left = 0 
    index_right = 0 

