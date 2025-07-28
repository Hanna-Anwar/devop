"""A shopkeeper purchase a product of rupees X  and sold the product at a profit of y% .find the selling price"""

product_price = int(input("enter the product price:"))

profit_in_perc = int(input("enter profit in %:"))

profit_amount = (profit_in_perc / 100) * product_price  #find profit

# print(profit_amount)

GST = 8

gst_amount = (product_price/ 100) * GST

# print(gst_amount)

selling_price =  product_price + profit_amount + gst_amount

print("selling price is ",selling_price)