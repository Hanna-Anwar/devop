
#path of the file to where we need to write

file_path = "C:\\Users\\hanna\\OneDrive\\Desktop\\devop\\python_works\\file_operation\\greetings.txt" 

fw = open(file_path,"w")

greeting_list = ["good morning","good afternoon","good evening","good night"]

for g in greeting_list:

    fw.write(g+"\n")