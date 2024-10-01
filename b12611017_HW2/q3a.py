numbers = [int(x) for x in input().split(",")]

for i in range(len(numbers)):
    for j in range(0, len(numbers) - 1 - i):
        if(numbers[j] > numbers[j + 1]):
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

unique_numbers = []
for num in numbers:
    if(num not in unique_numbers):
        unique_numbers.append(num)

print(",".join(str(x) for x in unique_numbers))
