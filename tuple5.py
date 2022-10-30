a = input("malumotni kiriting:")
lugat = {
    "Krasofka":{
        "a":["Jordan","2000yil"],
        "b": ["Nike","1999yil"]
    },
    "Hodie":{
        "a":["Hoddie","Malochniy"],
        "b":["Hoddie2","Qora"]
    },
    "Kurtka":{
        "a":["Gucci","2200$"],
        "b":["Channel","1800$"]
    }
}
if a.lower() == "Krasofka":
    print(lugat["Krasofka"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Krasofka"]["a"][0]) 
    elif b == "b":
        print(lugat["Krasofka"]["b"][1])    

elif a.lower() == "Hodie":
    print(lugat["Hodie"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Hodie"]["a"][0]) 
    elif b == "b":
        print(lugat["Hodie"]["b"][1])    


elif a.lower() == "Kurtka":
    print(lugat["Kurtka"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Kurtka"]["a"][0]) 
    elif b == "b":
        print(lugat["Kurtka"]["b"][1])    
    
    else:
        print("xato kiritdingiz")
        