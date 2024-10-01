first = input().split(",")
second = input().split(",")
result = []

for i in range(len(first)):
    for j in range(len(second)):
        if(first[i] == second[j]):
            result.append(str(first[i]))
            break
if(len(result) == 0):
    print("N/A")
else:
    print(",".join(result))
