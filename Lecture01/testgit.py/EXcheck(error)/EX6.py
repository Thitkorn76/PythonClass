def main():

    tatal = 0.0

    try:

        inflie = open('sales_data.txt', 'r')

        for line in inflie:

            amount = float(line)

            total += amount

        inflie.close()

    except Exception as err:
        print(err)

    else:
        print(format(total, '.2f'))

   

main()