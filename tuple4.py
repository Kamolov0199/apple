a = input("malumotni kiriting:")
lugat = {
    "Xolodilnik":{
        "a":["Artel","400$"],
        "b": ["Samsung","1000$"]
    },
    "Gazplita":{
        "a":["Gaz Plita1","1200$"],
        "b":["Gaz Plita2","3000$"]
    },
    "Dimavoy":{
        "a":["Dimavoy1","6000$"],
        "b":["Dimavoy2","1000$"]
    }
}
if a.lower() == "Xolodilnik":
    print(lugat["Xolodilnik"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Xolodilnik"]["a"][0]) 
    elif b == "b":
        print(lugat["Xolodilnik"]["b"][1])    

elif a.lower() == "Gazplita":
    print(lugat["Gazplita"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Gazplita"]["a"][0]) 
    elif b == "b":
        print(lugat["Gazplita"]["b"][1])    


elif a.lower() == "Dimavoy":
    print(lugat["Dimavoy"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Dimavoy"]["a"][0]) 
    elif b == "b":
        print(lugat["Dimavoy"]["b"][1])    
    
    else:
        print("xato kiritdingiz")
        