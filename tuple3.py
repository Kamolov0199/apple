a = input("malumotni kiriting:")
lugat = {
    "LG":{
        "a":["LG p40","200$"],
        "b": ["LG p30","100$"]
    },
    "Samsung":{
        "a":["Samsung Pro","2000$"],
        "b":["Samsung Lite ","1500$"]
    },
    "Artel":{
        "a":["ArtelTV1","200$"],
        "b":["ArtelTV2","150$"]
    }
}
if a.lower() == "LG":
    print(lugat["LG"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["LG"]["a"][0]) 
    elif b == "b":
        print(lugat["LG"]["b"][1])    

elif a.lower() == "Samsung":
    print(lugat["Samsung"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Samsung"]["a"][0]) 
    elif b == "b":
        print(lugat["Samsung"]["b"][1])    


elif a.lower() == "Artel":
    print(lugat["Artel"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Artel"]["a"][0]) 
    elif b == "b":
        print(lugat["Artel"]["b"][1])    
    
    else:
        print("xato kiritdingiz")
        