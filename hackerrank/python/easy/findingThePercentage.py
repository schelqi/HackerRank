if __name__ == '__main__':
    students_data = dict()
    students_count = int(input())
    for _ in range(students_count):
        student_name, *student_grades = input().strip().split(' ')
        students_data[student_name] = student_grades

    student_name = input().strip()
    grades = list(map(float, students_data[student_name]))
    grades_avg = sum(grades) / len(grades)

    print("%.2f" % grades_avg)
