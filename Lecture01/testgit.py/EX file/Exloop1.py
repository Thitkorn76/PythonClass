def main():

    sales_file = open('number.txt', 'r')


    line = sales_file.readline()

    while line != '':

        amout = float(line)

        print(format(amout, '.2f'))

        line = sales_file.readline()

        sales_file.close
    
main()