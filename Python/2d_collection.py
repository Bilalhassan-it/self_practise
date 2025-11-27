
groceries = [[123, "Banana", "Apple", "Pineapple"],
             ["Turkey", 1.2312, "Zinger"], 
             ["carrot", 'a', "onion"]]

for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()