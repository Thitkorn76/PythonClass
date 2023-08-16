def main():

    emp_file = open("employees.txt", 'r')

    line = emp_file.readline()
    
    while line != '':
        name =line.rstrip('\n')
        id_name = emp_file.readline().rstrip('\n')
        dept = emp_file.readline().rstrip('\n')

        print('Name:', name)
        print('ID:', id_name)
        print('Dept:', dept)

    line = emp_filee.readline()

    emp_file.close()

main()