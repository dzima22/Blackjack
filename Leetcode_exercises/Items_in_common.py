#items in common
def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
 
    for j in list2:
        if j in my_dict:
            return True
 
    return False
##items in common self implementation
list1 = [1,3,5]
list2 = [2,4,5]
def item_in_common(list1,list2):
    my_dict={}
    for i in list1:
        my_dict[i]=True
    for j in list2:
        if j in my_dict:
            return True
    return False

print(item_in_common(list1, list2))