keep_going = 'y'

while keep_going == 'y':
    whlesale = float(input("Enter the item's wholesale cost :"))
    retail_price = whlesale*2.5
    print("rerail price :",format(retail_price, ',.2f'))


    keep_going = input("Do you have another item?" + "(Enter y for yes) :")