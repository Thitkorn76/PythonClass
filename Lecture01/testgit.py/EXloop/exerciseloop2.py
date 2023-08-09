# This program calculates sales comission 
# Creat a variable to control the loop 
keep_going = 'y'

# Calculate a series of comission
while keep_going == 'y':
    # Get a salesperson's sales and commission eate.
    sales = float(input('Enter the amount of sales: '))
    comm_rate = float(input('Enter the amount of sales: '))

    # calculate tge commision.
    commisions = sales * comm_rate

    # Display the commision.
    print('The commission is $', \
    format(commisions, ',.2f'), sep ='') 
    
    # See of the user wants to do another one.
    keep_going = input('Do you want to calculate another' + 'commission (Enter y for yes): ')
                       