my_dict = {
    "Paul": "40",
    "Kate": "19",
    "Ben": "29",
    "Clive": "56"
}

print(my_dict)
del my_dict["Ben"]
print(my_dict)

my_dict = {
    "Paul": "40",
    "Kate": "19",
    "Ben": "29",
    "Clive": "56"
}

for key in my_dict.keys():
    print(f"key={key}")
    print(f"value={my_dict[key]}")

print(sorted(my_dict))