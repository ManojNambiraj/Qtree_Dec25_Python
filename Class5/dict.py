# Dict --> {key :  value} pair

student1 = {
    "name": "Raj",
    "age": 25,
    "dept": "IT", 
    "mobile": 9876543210,
    "isMale": True,
    "favColor": ("black", "red", "blue")
}

# data = [   #JSON
#     {
#         "name": "Raj",
#         "age": 25,
#         "dept": "IT", 
#         "mobile": 9876543210,
#         "isMale": True,
#         "favColor": ("black", "red", "blue")
#     }, 
#     {
#         "name": "Kavitha",
#         "age": 23,
#         "dept": "EEE", 
#         "mobile": 9876543210,
#         "isMale": True,
#         "favColor": ("black", "red", "blue")
#     }
# ]

# print(student1)
# print(student1["name"])
# print(len(student1))
# print(type(student1))
# print(student1["favColor"][0])

# print(student1.get("dept"))
# print(student1.keys())
# print(student1.values())

# student1["dept"] = "EEE"

# print(student1.items())
# print("depts" in student1)

# student1.update({"name": "Rajkumar"})
# student1["email"] = "raj@gmail.com"

# student1.pop("dept")
# student1.popitem()

# del student1
student1.clear()

print(student1)
