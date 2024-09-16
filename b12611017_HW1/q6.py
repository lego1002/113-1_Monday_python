import math

coefficent = input().split()
a = float(coefficent[0])
b = float(coefficent[1])
c = float(coefficent[2])

result_1 = (-b + math.sqrt(b * b - 4 * a * c)) / 2 / a
result_2 = (-b - math.sqrt(b * b - 4 * a * c)) / 2 / a

print(f"{max(result_1, result_2):.3f} {min(result_1, result_2):.3f}")









