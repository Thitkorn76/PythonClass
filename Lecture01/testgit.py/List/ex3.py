NUM_EMPLOYESS = 6

def main():

    hours = [0] * NUM_EMPLOYESS

    for index in range(NUM_EMPLOYESS):
        print("Enter the hours worked by employess", \
              index + 1,': ', sep='', end='')
        hours[index] = float(input())


    pay_rate = float(input('Enter the hourly pay rate: '))

    for index in range(NUM_EMPLOYESS):
        gross_pay = hours[index] * pay_rate
        print("Gross pay for employess", index + 1,': $', \
              format(gross_pay,'.2f'), sep='')
        
main()