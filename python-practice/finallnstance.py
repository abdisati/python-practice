# Importing a class library for json.
import json


#Creating a json dictionary consisting of string, integer, string array and boolean.





#Creating a json file and writing the python object content to the json.
with open("data.json", "w") as json_file:

    json.dump(data, json_file, indent=4)

print("Date has been written to data.json")

#This is going to load or open the json file as a read only.
with open("data.json", "r") as json_file:

    #Create an object called loaded_data. Load the json file into the argument parameter.
    loaded_data = json.load(json_file)

print("Succesfully able to read data.json")
print(loaded_data)



#Altering the json object or data.
loaded_data["age"] = 34 #ints
loaded_data["interests"].append("Secret Hobby")

#Rewrite the changes to the json file.
with open("data.json", "w") as json_file:

    json.dump(data, json_file, indent=4)

print("Date has been written to data.json")
print(loaded_data)





