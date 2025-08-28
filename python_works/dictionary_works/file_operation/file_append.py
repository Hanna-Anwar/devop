file_path = "C:\\Users\\hanna\\OneDrive\\Desktop\\devop\\python_works\\file_operation\\greetings.txt"

fa = open(file_path,"a")

food_item = ["idly","dosa","tea"]

for item  in food_item:

    fa.write(item +"\n")