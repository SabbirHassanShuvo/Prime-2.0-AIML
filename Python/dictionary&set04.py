info = {
    "name": "Dictionary and Set",
    "description": "Learn about dictionaries and sets in Python.",
    "topics": ["dictionaries", "sets"],
    "author": "John Doe",
    "is_free": True
}
# change the value of the "is_free" key to False
info["is_free"] = False
# add a new key-value pair to the dictionary
info["price"] = 19.99

# nested dictionary example
info["details"] = {
    "created_at": "2024-06-01",
    "updated_at": "2024-06-15"
}

#£££££££££££££ Dixtionary methods
# print(info.keys())
# print(len(info))
# print(info.values())
# print(info.items())
# print(info.get("name"))

# print(info)



# set example
fruits = {"apple", "banana", "orange", "apple", "banana"}
# add an element to the set
fruits.add("grape")
# remove an element from the set
fruits.remove("apple")

print(fruits)  # Output: {'apple', 'banana', 'orange'}