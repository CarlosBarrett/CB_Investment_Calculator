import math

print("investment" + " - to calculate the amount of your interest you'll earn on your investment")
print("bond" + "\t   - to calculate the amount you'll have to pay on a home loan")
#User makes selection of investment or bond
user_selection = input("\nEnter either 'investment' or 'bond' from the menu above to proceed:\n").lower()

if user_selection == "investment":
    money_amount = float(input("Enter the amount of money you wish to deposit: £"))
    interest_rate = float(input("Enter the percent of the interest rate: "))
    interest_rate = (interest_rate / 100) / 12
    number_years = int(input("Enter the number of years: "))
    interest = input("Would you like 'simple' or 'compound' interest?: ")
#investment calculations for simple and compound
    if interest == "simple":
        simple_interest = money_amount * (1 + interest_rate * number_years)
        total_simp = round(simple_interest, 2)
        print(f"Your simple interest after {number_years} years will be: £{total_simp}")
    elif interest == "compound":
        compound_interest = money_amount * math.pow((1 + interest_rate), number_years)
        total_comp = round(compound_interest, 2)
        print(f"Your compound interest after {number_years} years will be: £{total_comp}")
    else:
        print("you have made an invalid selection please try again")
#bond user inputs
if user_selection == "bond":
    house_value = float(input("Enter present house value: £"))
    interest_house = float(input("Enter the interest rate: "))
    interest_house = ((interest_house / 100) / 12) / 12
    number_months = int(input("Enter the amount of months to repay: "))
#bond repayment calculator
    bond_repayment = (interest_house * house_value) / (1 - (1 + interest_house) ** (- number_months))
    total_bond = round(bond_repayment, 2)
    print(f"Your total repayment will be: £{total_bond}")
else:
    print("you have made an invalid selection please try again")




    