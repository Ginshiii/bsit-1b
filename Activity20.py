#list

fruits = ["bananas", "apples", "guyabanos", "oranges", "avacado"]

#accesing an item

#INDEX - address / location
#              1          2         3             4         5
#fruits - ["bananas", "apples", "guyabanos", "oranges", "avacado"]

print(f"my favorite fruit is {fruits [2]}")
#how to addd another item onto the list
fruits.append("longgan")
print (fruits)
fruits.append("aratilis")
print(fruits)

#inserting an item on a specife index
fruits.insert(3, "chico")
print(fruits)