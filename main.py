import models
import csv
import functions as func

def start():
    print("Welcome to - Student Informatin System")
    print("1.List System\n2.Add Student\n3.Add Teacher\n4.Calculate GPA")
    selection = input()

    if selection == "1":
        print("1.Students\n2.Teachers")
        sub_selection = input()
        if sub_selection == "1":
            func.list_students()
        elif sub_selection == "2":
            func.list_teachers()
        else:
            print("Please choose valid manu item.")
    elif selection == "2":
        func.add_student()
    elif selection == "3":
        func.add_teacher()
    elif selection == "4":
        func.calc_gpa()
    else:
        print("Please choose valid menu item")
        start()


start()
