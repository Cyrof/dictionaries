#import lib 

# initialise var
directory = {}
counter  = 0

#search contact function 
def searchMenu():
    while True:
        print("Serch Contact: ")
        print("Search By: ")
        print("1. Name")
        print("2. Contact Number: ")
        print("3. Hobbies: ")
        print("0. Return to main menu")
        searchSelect = int(input("Your choice: "))
        if searchSelect == 0:
            break
        else:
            pass

#add contact function
def addContact():
    global directory
    hobbies = []

    print("Add Contact: ")
    name = input("Please enter the contact name: ").capitalize()
    add = input("Plaase enter the contact's address: ")
    num = int(input("Please enter the contact's mobile number: "))
    print("")
    while True:
        hobby = input("Please enter hobby (Enter 'end' to stop adding): ")
        print("")
        if hobby == "end":
            break
        else:
            hobbies.append(hobby)
        #directory.update({"name": name, "add":add, "num": num, "hobbies": hobbies})
        directory[name] = {"add":add, "num":num, "hobbies":hobbies}


#selection function 
def selectionMain(select):
    global counter
    if select == 1: 
        counter += 1
        addContact()
    elif select == 2:
        searchMenu()
    elif select == 3:
        pass
    elif select == 4:
        pass
    elif select == 5:
        pass
    else:
        print("Invalid selection")
        print("Please try again\n")
            

#checker function 
def checkdict():
    global directory
    if directory.keys():
        return True
    else:
        return False

#menu function 
def menu():
    global directory
    global counter
    while True:
        print("Welcome to my phone directory!")
        print("Number of contact in your directory: %d" %counter)
        print("These are the functions available:")
        print("1. Add new contact")
        print("2. Search for contact")
        print("3. Display all contact details in directory")
        print("4. Update existing contact details")
        print("5. Remove existing contact")
        print("0. Exit program")
        selectMain = int(input("Your selection please: "))
        print("")
        if selectMain == 2 or selectMain == 4 or selectMain == 5:
            if checkdict() == False:
                print("Selection is invalid\n")
                continue
            else:
                selectionMain(selectMain)
        if selectMain == 0:
            print(directory)
            break
        else:
            selectionMain(selectMain)



if __name__ == "__main__":
    menu()

