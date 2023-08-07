Name = input("Enter your first name :")
last_name = input("Enter your last name :")
ID_number = input("Enter your studant ID number :")
login_name = Name[0:3] + last_name[0:3] + ID_number[-3:]
print("Your system login name is :",login_name)
