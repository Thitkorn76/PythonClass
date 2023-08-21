def main():

    try:

        inflie = open('sales_data.txt', 'r')

        for line in inflie:

            amount = float(line)

            total += amount

        inflie.close()

        print(format(total,'.2f')) 

    except IOError:
        print('An error occured trying to read the file.')

    except ValueError:
        print('Non-numric data found in the file.')


    except:
        print('An error occured.')

main()