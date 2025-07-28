# Formula for EMI Calculation is -
# P x R x (1+R)^N / [(1+R)^N-1] where-
# P = Principal loan amount.
# N = Loan tenure in months.
# R = Monthly interest rate.,R = Annual Rate of interest/12/100.

loan_amount = int(input("enter loan amount : "))

annual_interest_rate = int(input("enter rate : "))

loan_tenure_yr = int(input("enter loan tenurs  : "))  #loan for how many years 

monthly_rate = annual_interest_rate/12/100

# print("monthly interest =",monthly_rate)

loan_tenure_month = loan_tenure_yr * 12

# print("tenure in month =",loan_tenure_month)

EMI = loan_amount * monthly_rate * (1 + monthly_rate) ** loan_tenure_month  / ((1 + monthly_rate) ** loan_tenure_month - 1)

print("emi =",EMI)

total_payable = EMI * loan_tenure_month

print("Total payable amount = ",total_payable)

total_interest = total_payable - loan_amount

print("total interest =",total_interest)


