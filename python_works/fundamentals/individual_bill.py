
# read total bill
# read no of dines
# read tip amount
# calculate individual split

total_bill = int(input("enter total bill :"))

dine = int(input("enter no of dines :"))

tip_amount = int(input("enter tip amount :"))

total=total_bill + tip_amount

individual_split = total / dine

print("individual split is ",individual_split)