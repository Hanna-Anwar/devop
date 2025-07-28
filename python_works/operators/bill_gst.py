# bill amount =>read bill amount
# dine count read_dinecount
# calculate tip as 12% of bill amount
# add 8% of gst along with bill amount
# calculate total amount and individual split



bill_amount = int(input("enter bill amount :"))

dine_count = int(input("enter dine count:"))

tip =  12

gst = 8

tip_amount = (tip /100) * bill_amount

GST_amount = (gst /100) *  bill_amount

total_cost = bill_amount + tip_amount + GST_amount

print("total cost is ",total_cost)

individual_amount = total_cost / dine_count

print("individual count is ",individual_amount)

