def main():

    salse_file = open('sales.txt', 'r')

    for line in salse_file:

        amount = float(line)

        print(format(amount, '.2f'))

    salse_file.close()

main()

