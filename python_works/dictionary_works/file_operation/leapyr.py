""" Task 1: Find Leap Years from a File
 Question:
 Create a file called years.txt containing a list of years. Write a program to read the years from the
 file and display only the leap years."""


file_path ="C:\\Users\\hanna\\OneDrive\\Desktop\\devop\\python_works\\file_operation\\year.txt"

fr = open(file_path,"r")

for yr in fr:

    int_yr = int(yr)

    if int_yr % 100 ==0 and int_yr %400 ==0 or int_yr%100 !=0 and int_yr%4==0:
        
        print(int_yr)