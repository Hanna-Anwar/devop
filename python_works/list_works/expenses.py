# Create a list expenses [10000,12000,13000,14000]

# update 12000 as 12500

# display all expenses

# display highest exoense

# display avg expenses

expenses = [10000,12000,13000,14000]

length = str(expenses)

expenses[1] = 12500

print(expenses)

# for i in range(0,len(expenses)):

#     print(expenses[i])

for e in expenses:

    print(e) #object

#method1

total_expenses= 0

for i in expenses:

   total_expenses +=i

print("method1 total-expense",total_expenses)


#method2

# for i in range(0,len(expenses)):

#     total_expenses += expenses[i]

# print("method2 total expenses",total_expenses)

# method3 

# total_expenses = sum(expenses)

print("method3 total expenses",total_expenses)

print("maximum expenses",expenses[-1])

print(max(expenses))

print(total_expenses/len(expenses))

