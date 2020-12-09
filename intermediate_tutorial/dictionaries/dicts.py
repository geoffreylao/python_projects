# Dictionary: Key-Value pairs, Unordered, Mutable
mydict = {
    "name": "Max",
    "age" : 28,
    "city" : "New York"
    }

print(mydict)

mydict["email"] = "max@xyz.com" # adding new elements to dict
print(mydict)

mydict["email"] = "coolermax@xyz.com" # reassigning dict element
print(mydict)

mydict.pop("age") # removes dict element
print(mydict)

if "name" in mydict: # if else with dict
    print(mydict["name"])
else:
    print("no name")

try: # try except with dict
    print(mydict["name"])
except:
    print("Error")

for key in mydict: # iterate through keys
    print(key)

for key in mydict.values(): # iterate through values
    print(key)

mydict_copy = dict(mydict) # how to copy dict

mydict2 = dict(name="Mary", age=27, city="Boston") # update dict with new values

mydict.update(mydict2)
print(mydict)

