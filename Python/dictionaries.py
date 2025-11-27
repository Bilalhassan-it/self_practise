# dictionary = a collection of {key:value} pairs
#              ordered and changeable. NO duplicates

capitals = {"Pakistan":"Islamabad", 
            "India":"New Delhi", 
            "Russia":"Moscow", 
            "USA":"New york", 
            "Turkey":"Istanbul"}

# print(dir(dict))
# print(help(dict))

# capitals.clear()
# capitals.get("Pakistan")
# capitals.pop("Turkey")
# capitals.popitem()
# capitals.update({"USA":"Nanga Parbat"})
# capitals.items()
# capitals.keys()
# capitals.values()

# if capitals.get("Pakistann"):
#     print("Pakistan is the LEGEND")
# else:
#     print("Not found!")

# for x, y in capitals.items():
#     print(f"{x} : {y}")

for collection in capitals.items():
    for item in collection:
        print(item, end = " ")
    print()

# print(capitals.keys())


