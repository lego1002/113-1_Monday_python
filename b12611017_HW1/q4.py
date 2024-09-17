entered_str = input()
sum = 0
for char in entered_str:
    if ('0' <= char <= '9'):
        sum += int(char)

print("{},{}".format(sum, len(entered_str)))
