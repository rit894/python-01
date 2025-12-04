mineral_data = {
    "Coal": {
        "Top Producer": "China",
        "Next Two": ["India", "US"],
        "Usage": ["Electricity", "Heating"]
    },
    "Iron Ore": {
        "Top Producer": "Australia",
        "Next Two": ["China", "Brazil"],
        "Usage": ["Construction", "Transportation"]
    },
    "Copper": {
        "Top Producer": "Chile",
        "Next Two": ["Peru", "China"],
        "Usage": ["Electronics", "Transportation"]
    },
    "Gold": {
        "Top Producer": "China",
        "Next Two": ["Australia", "Russia"],
        "Usage": ["Electronics", "Jewellery"]
    },
    "Silver": {
        "Top Producer": "Mexico",
        "Next Two": ["China", "Peru"],
        "Usage": ["Jewellery", "Coins", "Medicine"]
    },
    "Zinc": {
        "Top Producer": "China",
        "Next Two": ["Peru", "Australia"],
        "Usage": ["Batteries", "Paint", "Construction"]
    },
    "Nickel": {
        "Top Producer": "Indonesia",
        "Next Two": ["Philippines", "Russia"],
        "Usage": ["Batteries", "Coins", "Electronics"]
    },
    "Lithium": {
        "Top Producer": "Australia",
        "Next Two": ["China", "Argentina"],
        "Usage": ["Batteries", "Medicine"]
    },
    "Potash": {
        "Top Producer": "Canada",
        "Next Two": ["Russia", "Belarus"],
        "Usage": ["Fertilizer"]
    }
}
# question 1
def listofdict():
    x=list(mineral_data)
    return x

# Question 2
def UsedInfeilds():
    x=[]
    x1=[]
    for usages in mineral_data.values():
        for i in range(len(usages['Usage'])):
            x.append(usages["Usage"][i])

    return set(x)
print(UsedInfeilds())

# Question 3
def Top_Countries():
    x=[]
    x1=[]
    for usages in mineral_data.values():
        for i in range(len(usages["Next Two"])):
            x.append(usages["Top Producer"])
            x.append(usages["Next Two"][i])

    return set(x)
print(Top_Countries())

# Question 4
def mineralmapping(a):
    dict1={}
    for mineral , usage in mineral_data.items():
        for char in a:
            if char == usage["Top Producer"] or char in usage["Next Two"]:
                dict1[char]=dict1.get(char,0)+1
    print(dict1)
mineralmapping(Top_Countries())

# Question 5 
def demanding_feild(a):
    dict1={}
    for usage in mineral_data.values():
        for char in a:
            if char in usage['Usage']:
                dict1[char]=dict1.get(char,0)+1
    print(dict1)
    print(max(dict1.values()))
demanding_feild(UsedInfeilds())
    