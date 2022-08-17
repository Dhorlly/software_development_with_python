##
#Personal Income Tax Calculator
##

print("Personal Income Tax Calculator")
income = float(input("Enter your income: "))

if income <= 85528:
    tax = round(((income * 18)/100) - 556.02, 0)
    if tax < 0:
        print("The tax is: 0.0 thalers")
    else:
        print("The tax is: ", tax, "thalers")
else:
    tax = round(((income - 85528) * 32/100) + 14839.02, 0)
    print("The tax is:", tax, "thalers")
