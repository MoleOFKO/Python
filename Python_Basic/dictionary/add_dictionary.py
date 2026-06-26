# Change value of a specific item in dictionary
# Syntax : dictionary[key] = new_value
# Example 
flowers = {
    "name" : "Rose",
    "color" : "Red",
    "price" : 500
}
print("Before Changing : " , flowers)
#Change Values
flowers["price"] = 1000
print("After Changing : " , flowers)


# Update dictionary using update() method
# Syntax : dictionary.update({key1:value2, key2:value2,....})
flowers.update({"color" : "Pink" , "price" : 1500})
print("After Updating : ", flowers)


# Adding new item to dictionary 
# Syntax : dictionary[key] = value
flowers["origin"] = "Asia"
print("After Adding New Item :", flowers)

# Update dictionary using update() method
# Syntax: dictionary.update([key1:value1,key2:value2,...])
flowers.update({"color" : "Pink" , "price" : 1500})
print("After Updating : ", flowers )

#adding new item using update() method
flowers.update({"season" : "Spring"})
print("After Adding : ", flowers)