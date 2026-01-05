student = {
    "name" : " sonu kumar",
    " subject" : {
        "phy" : 97,
        " che " : 98,
        "math" : 95
    }
}
new_dict = { "city": "delhi"}
student.update(new_dict)

print(student)
# 
#  
collection = set()
collection.add(1)
collection.add(2)
collection.add("apnacollege")
collection.add((1, 2, 3))

collection.clear()
print(len(collection))
