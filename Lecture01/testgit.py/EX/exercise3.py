Houre_work = int(input("Enter your houre work :"))
pay_rate = int(input("Enter your pry rate :"))

if Houre_work >40:
    Bonus = ((Houre_work - 40)*1.5)*pay_rate + (40 * pay_rate)
    print("Bonus :", Bonus)
    
else :
    gross_pay = Houre_work*pay_rate
    print(("The goss pay is :"),gross_pay,)

