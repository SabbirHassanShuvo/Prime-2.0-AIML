# str = "Hello World"
# str1 = "I am a student"
# final = str + str1
# print(final)

# # length of string
# print(len(str))

# # string slicing
# print(str[1:11])
# print(str[5:])

# string functions
# str = "hello i am sabbir hassan shuvo im a student"
# result = str.endswith("student")
# result = str.capitalize()
# result = str.replace("student", "developer")
# result = str.find("student")
# result = str.count("student")
# print(result)


# Conditional statements
# if statement
from mimetypes import init


light = "green"

# if light == "green": 
#     print("You can cross the road")
# else:
#     print("You can not cross the road")


if light == "green":
    print("You can cross the road")
elif light == "yellow":
    print("You should wait")
elif light == "red":
    print("You can not cross the road")
else:    print("Invalid traffic light color")


marks = int(input('Enter your marks: '))

if marks >= 80:
    print("You got A+")
elif marks >= 70:
    print("You got A")
elif marks >= 60:
    print("You got A-")
elif marks >= 50:
    print("You got B")
elif marks >= 40:
    print("You got C")
elif marks >= 33:
    print("You got D")
else:    print("You got F")
