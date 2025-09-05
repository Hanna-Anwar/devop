file_path = "C:\\Users\\hanna\\OneDrive\\Desktop\\devop\\python_works\\file_operation\\employees.csv"

fr = open(file_path,"r")

all_employee = []

#reading each line

for line in fr:

    #removing \n from the end & splitting the line in to data using split , 

    data= line.rstrip("\n").split(",")

   

    #creating the dictionery using key: value pairs

    dictionery = {"id" : data[0],"name": data[1],
                  
                  "dept":data[2],"salary":data[3],

                  "email" : data[4],"location":data[5]
                  }
    
    # adding the dictioner to the list

    all_employee.append(dictionery)

print(all_employee)

#print names

names = [e.get("name") for e in all_employee ]

print(names)

# display the name who come from ekm

ekm_location = [e.get("name") for e in all_employee if e.get("location")== "ekm"]
    
print(ekm_location)

# display the name and mail who come from ekm

ekm_people = [(n.get("name"), n.get("mail")) for n in all_employee if n.get("location").lower()=="ekm"]#*********

print(ekm_people)


#print max salary

max_salary = max(all_employee,key =lambda e:e.get("salary"))
 
print(max_salary)

min_salary = min(all_employee,key =lambda e:e.get("salary")).get("salary")

min_sal_employee = [e.get("name") for e in all_employee if e.get("salary")==min_salary]

print(min_sal_employee)