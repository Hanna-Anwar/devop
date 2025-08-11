def odd_even_count(number): #123

    odd_count = 0

    even_count = 0

    while (number != 0 ):

      digit =  number %  10  #123% 10 =3

      if digit% 2 == 0: 
          
          even_count +=1

      else:
          
          odd_count +=1  #1
          
      number //= 10


    print("even count",even_count)
    print("odd count",odd_count)
 
 
    
odd_even_count(123)




