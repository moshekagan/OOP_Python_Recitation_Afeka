# part B
import csv


def print_all_student_from_csv():
    with open('lecture_1_students_2_grads.csv', newline='') as csvfile:
        read = csv.reader(csvfile)

        next(read)  # ignore fist line in the csv
        for row in read:
            print("name is ", row[0], "grade is ", row[1])


def read_csv_to_dict():
    with open('lecture_1_students_2_grads.csv', newline='') as csvfile:
        read = csv.reader(csvfile)
        students = {}

        next(read) # ignore fist line in the csv
        for row in read:
            students[row[0]] = row[1]

        return students


def find_common_grade(students):
    common = {}

    for grade in students.values():
        if grade in common:
            common[grade] += 1
        else:
            common[grade] = 1

    grade = max(common, key=common.get)

    return grade


def find_avg(students):
    sum = 0
    for grade in students.values():
        sum += int(grade)

    return sum / len(students)


def students_with_common_grade(students, common_grade):
    common_students = []

    for name, grade in students.items():
        if common_grade == grade:
            common_students.append(name)

    return common_students


def add_student_to_csv(name, grade):
    with open('lecture_1_students_2_grads.csv', 'a+', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow([name, grade])
        csvfile.close()


def main():
    print_all_student_from_csv()
    students = read_csv_to_dict()
    print() # empty line

    common_grade = find_common_grade(students)
    print(f"The most common grade is: {common_grade}")
    print(f"The Students with the common grades are: {students_with_common_grade(students, common_grade)}")

    print()  # empty line
    print(f"The average grades is: {find_avg(students)}")

    print()  # empty line
    add_student_to_csv("Jerry", 91)
    print_all_student_from_csv()

if __name__ == '__main__':
    main()



