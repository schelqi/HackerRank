from collections import namedtuple
if __name__ == '__main__':
    students = list()
    total_marks = 0
    N = int(input())
    params = input().strip()
    Student = namedtuple("Student", params)
    for _ in range(N):
        values = input().strip().split()
        students.append(Student(*values))
    for student in students:
        total_marks += int(student.MARKS)

    print("%.2f" % (total_marks/N))

