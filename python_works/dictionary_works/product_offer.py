product = {
"code":"kt12345",
"title":"Linenshirt",
"brand":"usPollo",
"price":2300,
# "offer":1000
}

print(product)
#add offer is 1000 if offer not exist else add 500 to the current offer

if "offer" in product:

    product["offer"]+= 500 #update
    
else:

   product["offer"] = 1000  #add

print(product)

