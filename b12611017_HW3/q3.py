#base_path = "/home/lego/Desktop/examples/"
file_name = input()
H_score = 0
H_student_num = 0

#with open(base_path + file_name, "r") as file:
with open(file_name, "r") as file:
    N = int(file.readline().strip())

    for _ in range(N):
        line = file.readline().strip()
        parts = line.split()
        student_num = int(parts[0])
        scores = list(map(int, parts[1:]))
        total_score = sum(scores)

        if(total_score > H_score):
            H_score = total_score
            H_student_num = student_num

print("{},{}".format(H_student_num, H_score))
