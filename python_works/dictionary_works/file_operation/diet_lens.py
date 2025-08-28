file_path = "C:\\Users\\hanna\\OneDrive\\Desktop\\devop\\python_works\\file_operation\\food_log.csv"

fr = open(file_path,"r")

food_log = []

for line in fr:

    data = line.rstrip("\n").split(",")

    # print(data)

    if len(data) >1:

        dictionery = {
                        "date" :data[0],
                        "meal_type":data[1],
                        "name":data[2],
                        "serving_size":data[3],
                        "calories":data[4]
 
                    }

        food_log.append(dictionery)

print(food_log)

daily_summery = {}

for e in food_log: #{'date': '2025-08-22', 'meal_type': 'Breakfast', 'name': 'Poha', 'serving_size': '1 plate', 'calories': '280'}

    date = e.get("date")

    calories = int(e.get("calories"))

    if date in daily_summery:

        daily_summery[date]+=calories

    else:

        daily_summery[date] =calories

print(daily_summery)

max_calory = max(daily_summery,key =lambda c:c.get("calories") )

print(max_calory)