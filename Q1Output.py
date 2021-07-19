students = {}

#add student function 
def addStudent():
    global students
    print("Add new Student to dictionary")
    studentName = input("Enter Student name: ")
    studentCourse = input("Enter Student course: ")
    studentGpa = float(input("Enter Student GPA: "))

    

#selector function 
def selector(choice):
    if choice == 1:
        pass
    elif choice == 2:
        pass
    else:
        print("Invalid choice")

#menu function 
def menu():
    while True:
        print("1. Add new student")
        print("2. Show dictionary")
        print("0. Exit")
        choice = input("Your choice: ")
        if choice == 0:
            break
        else:
            pass
