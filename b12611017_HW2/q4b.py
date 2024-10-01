def find_common_elements(list1, list2):
    common_elements = set(list1) & set(list2)
    if(common_elements):
        return list(common_elements)
    else:
        return []

list1 = input().split(",")
list2 = input().split(",")
result = find_common_elements(list1, list2)

if(result):
    for i in range(len(result)):
        for j in range(0, len(result) - 1 - i):
            if(result[j] > result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
    print(",".join(result))
else:
    print("N/A")
