all_student_path = "C:\\Users\\hanna\\OneDrive\\Desktop\\devop\\python_works\\file_operation\\all_students.txt"

failed_student_path = "C:\\Users\\hanna\\OneDrive\\Desktop\\devop\\python_works\\file_operation\\failed_stud.txt"

passes_stud_path = "C:\\Users\\hanna\\OneDrive\\Desktop\\devop\\python_works\\file_operation\\passed_stud.txt"

f_all_stud_ref = open(all_student_path,"r")

f_failed_stud_ref = open(failed_student_path,"r")

f_passes_stud_ref = open(passes_stud_path,"w")

all_stud_set = set()

fail_stud_set = set()

for name in f_all_stud_ref:

    all_stud_set.add(name.rstrip("\n"))

print(all_stud_set)

for name in f_failed_stud_ref:

    fail_stud_set.add(name.rstrip("\n"))

print(fail_stud_set)

passed_stud = all_stud_set.difference(fail_stud_set)

print(passed_stud)

for name in passed_stud:

    f_passes_stud_ref.write(name+"\n")