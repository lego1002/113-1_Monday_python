numbers = [int(x) for x in input().split(",")]

unique_numbers = list(set(numbers))

for i in range(len(unique_numbers)):
    for j in range(0, len(unique_numbers) - 1 - i):
        if unique_numbers[j] > unique_numbers[j + 1]:
            unique_numbers[j], unique_numbers[j + 1] = unique_numbers[j + 1], unique_numbers[j]

print(",".join(str(x) for x in unique_numbers))
