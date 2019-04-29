# Module 3
#   Programming Assignment 4
#     Prob-2.py

# Cody Martin

'''
Your IPO comment goes here
input: Name, Wage, hours from year
Process: Based on the input, multiple the hours by wages. Anything over 40 hours get paid 1.5x more then regular pay.Then we deduct the taxs and medical.
output: The name, overtime pay(if any) regular pay, tax deduction, medical deduction and then the take home pay

'''


def main():
    name = input("What is your name? ")
    wage = eval(input("How many dollars per hour do you make? "))
    hours = eval(input("How many hours did you work this week? "))
    tax = .20
    medical = .10


# This will decide how to convert the wages dependant on if overtime was worked or not

    if hours > 40:
        overhours = (hours - 40)
        overpay = (wage * 1.5)
        overtimePay = (overhours * overpay )
        regularhours = (hours - overhours)
        regular1 = (regularhours * wage)
        taxwithheld = ((overtimePay + regular1) * tax)
        medicalwithheld = ((overtimePay + regular1) * medical)
        totalwithheld = (taxwithheld + medicalwithheld)
        print()
        print(name)
        print("Overtime Pay:        $", overtimePay)
        print("Regular Pay:         $", regular1)
        print("Tax Withheld:        $", taxwithheld)
        print("Medical Withheld:    $", medicalwithheld)
        print("Take Home Pay:       $", overtimePay + regular1 - totalwithheld)
        print()

 # if overitme was ot worked, this code will calculate wages earned at regular pay
    else: 
        regular = (wage * hours)
        taxes = (regular * tax)
        medi = (regular * medical)
        takehome = (regular - taxes - medical)
        print()
        print(name)
        print("Regular Pay:         $",regular)
        print("Tax Withheld:        $", taxes)
        print("Medical Withheld:    $",medi)
        print("Take Home Pay:       $", takehome)
        print()





main()