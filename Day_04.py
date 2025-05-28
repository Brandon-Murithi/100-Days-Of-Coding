student = { #student is a dictionary
    "name": "Brandon",
    "age": 20,
    "grade":"A"
}
print(student)
print(student["age"])
student["university"]= "Riara" #adding a new key-value pair/ using .append() method is for lists, not dictionaries
print(student)

student["sex"]="male"
print(student)

print(f"{student["name"]}\n "
      f"{student["age"]}\n")

print(f"Jesus\nis\nKing")

print(student.get("name"))
print(student.get("sex"))
print(student.get("age"))
print(student.keys())#returns all the keys in the dictionary
print(student.values()) #this one returns all the values in the dictionary.
print(student.items())

print(f"{student["name"]}\n"
      f"{student["age"]}\n"
      f"{student["sex"]}\n"
      )

#Personal dictionaty

contacts = {}
   
contacts = {
    "name": "Tracy"
    

}

contacts['number'] = 722222222
print(contacts)

parking_system = {}
parking_system = {
    "car brand": "Mercedes",
    "plate number": 234
}

EPL_fixture={}
EPL_fixture = {
    "home team": "Manchester City",
    "away team": "Manchester United"
}
print(EPL_fixture)

print(
    f"{EPL_fixture["home team"]}\n"
    f"{EPL_fixture["away team"]}\n"
)

EPL_fixture["day"]="Wednesday"
print(EPL_fixture)

EPL_fixture.get("home team")
EPL_fixture.keys()
EPL_fixture.values()




phonebook = {}
phonebook["Alice"] = "123-4567"
phonebook["Bob"] = "987-6543"

# Retrieve information
name = input("Enter a name to look up: u")
if name in phonebook:
 print("found") 
else: print(" not found.")


#Another my own thinking from what I've learnt
house = {}
house = {
 "tables":4,
 "chairs": 10
}
print(house)

print(
 f"{house["chairs"]}\n"
 f"{house["tables"]}\n"
)

house["rooms"] =9
print(house)

house.get("chairs")
house.keys()
house.values()