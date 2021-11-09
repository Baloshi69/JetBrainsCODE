import math

# write your code here

# Asking User what performer,
print("What do you want to calculate?")
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payments amount,')
print('type "p" for the monthly payment')

loan_type = input()  # saving user input

# if user input match "n" we will calculate number monthly payments needed to repay.
if loan_type == "n":
    loan_principal = int(input('Enter the loan principal:'))  # Getting saving Principal loan.
    mon_pay = int(input('Enter the monthly payment:'))        # Getting Monthly payment rate.
    loan_interest = float(input('Enter the loan interest:'))   # Getting interest rate, from user
    nominal_interest = loan_interest / (12 * 100)               # Calculating Nominal Interest

    # Below I am calculating number of month, needed to repay loan.
    mon_repay = math.ceil(math.log((mon_pay / (mon_pay - (nominal_interest * loan_principal))), 1 + nominal_interest))

    # Calculating years and months below, needed to repay.
    years = mon_repay // 12
    months = mon_repay % 12

    # Evaluating, if month is > 0, then it means you need years and month, else you will pay only in  years,
    if years > 0 and months > 0:
        print(f"it will take {years} years, and {months} months to repay the loan")
    elif year <= 0 and month  > 0:
        print(f"it will take {months} months to repay the loan")
    else:
        print(f"it will take {years} years to repay this loan!")

# if user input match "a" we will calculate Ordinary Annuity payments.
elif loan_type == "a":
    loan_principal = int(input("Enter the loan principal:"))  # Getting saving Principal loan.
    num_of_mon = int(input("Enter the number of periods:"))   # Getting numbers of month to repay loan.
    loan_interest = float(input("Enter the loan interest:"))   # Getting Interest rate from user.
    nominal_interest = loan_interest / (12 * 100)               # calculating Nominal Interest rate.

    # Below I am calculating Ordinary Annuity payments.
    annuity = loan_principal * ((nominal_interest * math.pow((1 + nominal_interest), num_of_mon)) / (
                math.pow((1 + nominal_interest), num_of_mon) - 1))
    annuity = math.ceil(annuity)                                    # Rounding up the float numbers.
    print(f"Your monthly payment = {annuity}!")                     # Printing out the calculation. to user

# If user input match "p" we will calculate Principal Loan Amount.
elif loan_type == "p":
    annuity = float(input("Enter the annuity payment:"))        # Getting Annuity from user.
    num_of_mon = int(input("Enter the number of period:"))      # Getting number of month to repay loan.
    loan_interest = float(input("Enter the loan interest:"))     # Getting Interest rate from user.
    nominal_interest = loan_interest / (12 * 100)                 # calculating Nominal Interest rate.

    # Below we calculating, Loan principal, and rounding up it
    loan_principal = round(annuity / ((nominal_interest * math.pow((1 + nominal_interest), num_of_mon)) / (
                math.pow((1 + nominal_interest), num_of_mon) - 1)))

    print(f"Your loan principal = {loan_principal}!")           # Printing out the Principal Loan Amount.
