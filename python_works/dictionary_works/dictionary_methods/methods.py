fruits = {

    "a":"apple",
    "b":"banana",
    "c":"cherry",
    "d":"dragon fruit"
}

print(f"complete dictionary {fruits}")

print(fruits.get("c"))

popped_value = fruits.pop("d")

print(popped_value)

print(f"fruits after popped {fruits}")

key = fruits.keys()

fruits.update(o="orange",e="egg-fruit")

# fruits.update(e="egg-fruit")

print(fruits)

for k in key:

    print(k)

for v in fruits.values():

    print(f"values are {v}")

for k,v in fruits.items():

    print(k,v)
