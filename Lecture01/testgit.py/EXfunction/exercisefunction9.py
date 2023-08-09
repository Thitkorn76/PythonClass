Discount_Percentage = 0.20

def main():
    reg_price = get_regular_price()
    sale_price = reg_price - Discount_Percentage
    print("The sale price is $", format(sale_price,'.2f'), sep='')

def get_regular_price():
    price = float(input("Enter the item's regular price: "))
    return price 

def discout(price):
    return price * Discount_Percentage

main()