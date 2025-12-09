my_List = [3,5,1,7,0,9,11]


def list_split(my_List):
    left_list = my_List[:(len(my_List))]
    right_list = my_List[(len(my_List)):]

    left_list = list_split(left_list)
    right_list = list_split(right_list)

    mergedList = merge_sort(left_list,right_list)
    return mergedList

def merge_sort():

    merged = [] 
    index_left = 0 
    index_right = 0 

