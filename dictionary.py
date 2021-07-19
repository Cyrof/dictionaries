contact = {
    "person1": ["John", "abc lane", "18945348"],
    "hobby1": ["hiking", "jogging"],
    "person2": ["tim", "def lane", "65459156"],
    "hobby2": ["hiking", "swimming"],
}



contactnew = {
    "John" : {"add" : "abc lane", "tel":"18945148", "hobby":["hiking", "joggin"],},
}

contactnew.update(Tim = {"add":"def lane", "tel":"65459156", "hobby":["hiking","swimming"],})

# contactnew = {}

if contactnew:
    print("have items")
else:
    print("no items")
