sachin_friends = ["rahul","ganguly","yuvi","raina","zaheer","dhoni","laxmen"]

dhoni_friends =  ["rahul","ganguly","yuvi","raina","zaheer","sachin","kholi"]


st1  = set(sachin_friends)

st2 = set(dhoni_friends)

all_user=st1.union(st2)

print(all_user)

#display unique friend of sachin

unique = st1.difference(st2)

print(unique)

#mutual frinds count

mutual_friends = st1.intersection(st2)

# print(intersection)

print(len(mutual_friends))





