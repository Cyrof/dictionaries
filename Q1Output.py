#initialise variable
students = {}
counter = 0

#add student function 
def addStudent():
    global students
    global counter 
    print("Add new Student to dictionary")
    studentName = input("Enter Student name: ")
    studentCourse = input("Enter Student course: ")
    studentGpa = float(input("Enter Student GPA: "))

    name = "student" + str(counter)
    students[name] = {"name":studentName, "Course":studentCourse, "GPA":studentGpa}
    counter += 1
    

#show dictionary function 
def showdict():
    global students
    print(students)


#selector function 
def selector(choice):
    if choice == 1:
        addStudent()
    elif choice == 2:
        showdict()
    else:
        print("Invalid choice")

#menu function 
def menu():
    while True:
        print("1. Add new student")
        print("2. Show dictionary")
        print("0. Exit")
        choice = int(input("Your choice: "))
        if choice == 0:
            break
        else:
            selector(choice)

if __name__ == "__main__":
    menu()