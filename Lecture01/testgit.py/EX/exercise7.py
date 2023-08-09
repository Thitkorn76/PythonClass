from tkinter import MULTIPLE


print("plase select operation \n 1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide")


opera_tion = int(input("select operations 1, 2, 3, 4, :"))
first_name = int(input("Enter first number :"))
second_number = int(input("Enter your score :"))

if opera_tion == 1:
    add = (first_name + second_number)
    print(first_name, '+' ,second_number, '+' ,add)

elif opera_tion == 2:
    subtract = (first_name - second_number)
    print(first_name, '-' ,second_number, '=' ,subtract)

elif opera_tion == 3:
    Multiply = (first_name*second_number)
    print(first_name, '*' ,second_number, '=' ,Multiply)

elif opera_tion == 4:
    Divide = (first_name / second_number)
    print(first_name, '//' ,second_number, '=' ,Divide)

else:
    print("Error")

