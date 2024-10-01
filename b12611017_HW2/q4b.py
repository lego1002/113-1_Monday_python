def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    if(common_elements):
        return(",".join(common_elements))
    else:
        return("N/A")

list1 = input().split(",")
list2 = input().split(",")

result = find_common_elements(list1, list2)
print(result)
