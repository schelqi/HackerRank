# Given the names and grades for each student in a class of N students, store them in a nested list
# and print the name(s) of any student(s) having the second-lowest grade.


if __name__ == '__main__':
    students_count = int(input())
    students_scores = list()
    grades_set = set()
    for _ in range(students_count):
        student_name = input().strip()
        student_score = float(input().strip())
        students_scores.append([student_name, student_score])
        grades_set.add(student_score)

    # Calculate the second-lowest grade
    grades = list(grades_set)
    grades.sort()
    second_lowest_grade = grades[1]
    # find students with second-lowest grade
    students_with_second_lowest_grade = [row[0] for row in students_scores if row[1] == second_lowest_grade]
    students_with_second_lowest_grade.sort()

    print(*students_with_second_lowest_grade, sep="\n")
