def get_name():
    first = input("Enter your first name:")
    last = input("Enter your last name")

    return first,last

first_name, lastname = get_name()
print("First name:" ,first_name,"last name:", lastname)