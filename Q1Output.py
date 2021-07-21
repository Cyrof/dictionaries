#initialise variable
students = {}
counter = 0

# Gpa = (gpa of mod * credit score (total grade point)) / total credit score

#function to calculate student gpa 
def calGPA():
    totalcredit = 0
    totalgradepoint = 0
    moduleNum = int(input("How many modules did the student take: "))
    print("")
    for x in range(moduleNum):
        gpaformod = float(input("Enter gpa for module %d: " % x))
        creditscore = int(input("Enter credit score for module %d: " % x))
        print("")
        totalcredit += creditscore
        totalgradepoint += (gpaformod * creditscore)
    gpa = totalgradepoint / totalcredit
    return gpa


#add student function 
def addStudent():
    global students
    global counter 
    print("Add new Student to dictionary")
    studentName = input("Enter Student name: ")
    studentCourse = input("Enter Student course: ")
    ask = input("Do you know the student's GPA? [y/n]: ")
    name = "student" + str(counter)
    if ask.lower() == "n":
        gpa = format(calGPA(), '.2f')
        students[name] = {"name":studentName, "Course":studentCourse, "GPA":gpa}
    else:
        studentGpa = float(input("Enter Student GPA: "))
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