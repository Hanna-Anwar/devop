file_path = "C:\\Users\\hanna\\OneDrive\\Desktop\\devop\\python_works\\dictionary_works\\file_operation\\emp_details.csv"

fr = open(file_path,"r")

emp_list = []

for line in fr:

    data = line.rstrip("\n").split(",")

    dictionery ={

   "job-id" : data[0],
   "company-name": data[1],
   "job-title" : data[2],
   "location" : data[3],
   "job-type" : data[4],
   "salary" :data[5],
   "posted-date" : data[6]

    }

    emp_list.append(dictionery)

print(emp_list)


#print company name give fulltime

full_time_job = [e.get("company-name") for e in emp_list if e.get("job-type").lower()=="full-time"]

#{'job-id': '101', 'company-name': 'Google', 'job-title': 'Software Engineer', 'location': 'Bangalore', 'job-type': 'Full-time', 'salary': '"Ã¢â€šÂ¹15', 'posted-date': '00'}

print(full_time_job)

#print company names located in kochi

kochi_located_company = [e.get("company-name") for e in emp_list if e.get("location").lower()=="kochi".lower()]

print(kochi_located_company)