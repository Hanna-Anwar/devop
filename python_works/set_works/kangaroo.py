#kangaroo word(all the characters of the target word are  derived from source word also order also need to m)


source = "observe"

target = "serve"


for ch in source:

 for ch1 in target:

    if ch == ch1:
      
      print("kangaroo")
      
    break
 
else:
   
    print("not")
