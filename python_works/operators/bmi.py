
# calculate BMI ?

# read height in cm

# read weight in kg

# BMI formula = weight in kg / height in m ** 2



weight_in_kg = int(input("enter weight in kg:"))

height_in_cm = int(input("enter height in cm:"))

# conversion of cm to m

height_in_m= height_in_cm / 100

BMI = weight_in_kg / height_in_m ** 2

print("BMI of a person with height",height_in_cm,"and weight",weight_in_kg,"is ",BMI)