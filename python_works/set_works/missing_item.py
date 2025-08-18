ware_house = {"laptop","mouse","key_board","wifi-adapter","mic","speaker","projector"}

actual_items = {"laptop","mouse","key_board"}

missing_items = ware_house.difference(actual_items)

#find missing item

print(missing_items)