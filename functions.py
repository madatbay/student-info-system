import csv

def list_students():
    with open('db/students.csv','rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 1
        for row in csv_reader:
            print(line_count,".",f'Student Name: {row[0]}\nFaculty: {row[1]}\nAge: {row[2]}\nGPA: {row[3]}')
            line_count += 1
        print(f'Total element number : {line_count -1}')

def list_teachers():
    with open('db/teachers.csv','rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 1
        for row in csv_reader:
            print(line_count,".",f'Teacher Name: {row[0]}\nAge: {row[1]}\nFaculty: {row[2]}\nSalary: {row[3]}')
            line_count += 1
        print(f'Total element number : {line_count -1}')

def add_student():
    name = input("Full Name: ")
    faculty = input("Faculty: ")
    age = input("Age: ")
    gpa = input("GPA: ")

    with open('db/students.csv', mode='a',newline='\n') as csv_file:
        csv_writer = csv.writer(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,faculty,age,gpa])

def add_teacher():
    name = input("Full Name: ")
    faculty = input("Faculty: ")
    age = input("Age: ")
    salary = input("GPA: ")

    with open('db/students.csv', mode='a',newline='\n') as csv_file:
        csv_writer = csv.writer(csv_file,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,faculty,age,salary])

def calc_gpa():
    perf1 = int(input("PERF 1: "))
    perf2 = int(input("PERF 2: "))
    perf3 = int(input("PERF 3: "))
    att = int(input("Attendance: "))
    pw = int(input("Personal work:"))
    final = int(input("Final:"))
    total = perf1 * 0.1 + perf2 * 0.1 + perf3 * 0.1 + att * 0.1 + pw * 0.1 + final * 0.5
    print("Your semester GPA: ", round(total))