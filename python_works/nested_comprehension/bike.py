bikes=[

    ["passion-pro","hero",89000,"petrol",125],
    ["passion-plus","hero",89000,"petrol",125],
    ["activa","honda",120000,"petrol",125],
    ["xpulse","hero",139000,"petrol",150],
    ["hunter","re",200000,"petrol",350],
    ["metor","re",230000,"petrol",350],
    ["triumph-speed-400x","triumph",300000,"petrol",400],
    ["s1-pro","ola",140000,"ev",120],
    ["ather450x","ather",160000,"ev",150]

]

#all bike names

all_names = [b[0] for b in bikes]

print(all_names)

#all bike price

all_bike_price = [b[2]  for b in bikes]

print(all_bike_price)

#all bike varient 

all_bike_varient = {b[3] for b in bikes}

print(all_bike_varient)

#price filter

price_filter =[b[0] for b in bikes if b[2]<120000]

print(price_filter)

ev_bikes = [b[0] for b in bikes if b[3]=="ev"]

print(ev_bikes)


def get_price(lst):

    return lst[2]

costly_bike = max(bikes,key=get_price)

print(costly_bike)

low_price_bike = min(bikes,key=get_price)

print(low_price_bike)
