a = input("malumotni kiriting:")
lugat = { 
    "Direktor":{
        "a":["Muhammadjon ","Kamolov"],
        "b":["Jalol","Sarvarov"]
},
    "Quruvchi":{
        "a":["Amlena","Svami"],
        "b":["Shoxa","Dobriy"],
},  "Dasturchi":{
        "a":["Jumayev","Ubadullo"],
        "b":["Victus","Hp"]
},

}

if a.lower() == "Direktor":
    print(lugat["Direktor"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Direktor"]["a"][0]) 
    elif b == "b":
        print(lugat["Direktor"]["b"][1])


if a.lower() == "Quruvchi":
    print(lugat["Quruvchi"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Quruvchi"]["a"][0]) 
    elif b == "b":
        print(lugat["Quruvchi"]["b"][1])    
    
    

if a.lower() == "Dasturchi":
    print(lugat["Dasturchi"])
    b = input("sizga qaysi biri kerak:")
    if b == "a":
        print(lugat["Dasturchi"]["a"][0]) 
    elif b == "b":
        print(lugat["Dasturchi"]["b"][1])   
    
    else:
        print("xato kiritdingiz")