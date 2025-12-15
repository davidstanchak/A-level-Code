def merge_sort(left,right):

    merged = [] 
    index_left = 0 
    index_right = 0 

    while index_left < len(left) and index_right < len(right):
        if left[index_left] < right[index_right]:
            merged.append(left[index_left])
            index_left += 1
        else:
            merged.append(right[index_right])
            index_right += 1

    while index_left < len(left):
        merged.append(left[index_left])
        index_left += 1

    # Add to the merged list any remaining data from right list
    while index_right < len(right):
        merged.append(right[index_right])
        index_right += 1

    return merged

def list_split(items):

    if len(items) <= 1:
        return items
    midpoint = (len(items)-1) //2
    left_list = items[:midpoint+1]
    right_list = items[midpoint+1:len(items)]

    left_list = list_split(left_list)
    right_list = list_split(right_list)
  
    merged_items = merge_sort(left_list,right_list)

    return merged_items

my_list = [6,3,7,0,1,4,5]

print(list_split(my_list))
