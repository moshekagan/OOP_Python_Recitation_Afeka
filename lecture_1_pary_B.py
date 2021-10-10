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


def main():
    print_all_student_from_csv()
    students = read_csv_to_dict()
    print(students)

    print("The most common grade is: " + find_common_grade(students))


if __name__ == '__main__':
    main()



