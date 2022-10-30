a = input("malumotni kiriting:")
lugat = { 
    "Spartivni":{
        "a":["Bugatti ","126700$"],
        "b":["Bugatti cheyron","145000$"]
},
    "Viduxa":{
        "a":["Koinseg","4500000$"],
        "b":["Koinseg Pro","120000000$"],
},  "Comfort":{
        "a":["RovseRoyce","1000000000000"],
        "b":["RovseRoyce Elite","100000000000000"]
},

}

if a.lower() == "Spartivni":
    print(lugat["Spartivni"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Spartivni"]["a"][0]) 
    elif b == "b":
        print(lugat["Spartivni"]["b"][1])

    else:
        print("xato kiritdingiz")

if a.lower() == "Viduxa":
    print(lugat["Viduxa"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Viduxa"]["a"][0]) 
    elif b == "b":
        print(lugat["Viduxa"]["b"][1])    
    
    else:
        print("xato kiritdingiz")

if a.lower() == "Comfort":
    print(lugat["Comfort"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Comfort"]["a"][0]) 
    elif b == "b":
        print(lugat["Comfort"]["b"][1])   
    
else:
    print("xato kiritdingiz")







