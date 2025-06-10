if __name__ == '__main__':
    grades_count_per_student, students_count = map(int, input().strip().split(' '))
    students_grades = list()
    for _ in range(students_count):
        students_grades.append(list(map(float, input().strip().split(' '))))

    zipped_grades = zip(*students_grades)
    for row in zipped_grades:
        print(sum(row)/students_count)
