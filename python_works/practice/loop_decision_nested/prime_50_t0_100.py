
for num in range(50,101):

  is_prime = True

  for i in range(2,num):

        if num % i == 0:
             
            is_prime = False
             
            break   
        
  if is_prime == True:

    print(num)

       

           

            
           
   