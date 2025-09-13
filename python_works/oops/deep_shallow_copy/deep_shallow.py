from copy import copy,deepcopy


meghana_fav_food =[

    ["meals","sambar"],
    ["biriyani","lime"],
    ["burger","cold-coffee"]
]



nandana_fav_food = deepcopy(meghana_fav_food) #deep copy

# nandana_fav_food=copy(meghana_fav_food)  #shallow copy

nandana_fav_food[0][0]="dosa"

print(nandana_fav_food)

print(meghana_fav_food)