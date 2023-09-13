print("Plase select operation", '\n' ,"1.Display Heroes", '\n' ,"2.Add Heroes", '\n' ,"3.insert Heroes", '\n' ,"4.Remove Heroes", '\n' ,"5.Display Sortes Heroes(Ascending/Descending)")

Heroes = []
opera_tion = int(input("select operation 1, 2, 3, 4 :"))
    
def Display_Hero():

    print(Heroes)

def Add_Hero():

    Heroes.append(input(""))

def Insert_Hero():

    Heroes.insert(int(input())),Heroes(int(input()))

def remove_Hero():

    Heroes.remove(input(""))

def sort_Hero():

    opera_tion = int(input())

    if opera_tion == 1 :
        Heroes.sort()
        print(Heroes)

    elif opera_tion == 2:
        Heroes.sort()
        Heroes.reverse
        print(Heroes)

def loopfunc():

    if opera_tion == 1:
        Display_Hero()

    elif opera_tion == 2:
        Add_Hero()

    elif opera_tion == 3:
        Insert_Hero()

    elif opera_tion == 4:
        remove_Hero()

    elif opera_tion == 5:
        sort_Hero()

loopfunc()

again = 'y'

while again.lower() == 'y':
    opera_tion = (int(input("Plase select menu from above: ")))
    loopfunc()
    again = input("Enter more data? (y/n): ")        