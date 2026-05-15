# Read file demo.txt
# f = open("demo.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

# write to file demo.txt
# f = open("Python/demo.txt", "w")
# f.write("This is a demo file.\n")

# This will overwrite the existing content of the file. If you want to append to the file, use "a".
# f = open("Python/demo.txt", "a")
# f.write("This is this third line.\n")
# f.close() 


# with open statement
# with open("Python/demo.txt", "r") as f:
#     data = f.read()
#     print(data)
#     print(type(data))


# Delete a file
import os
# os.remove("Python/demo.txt")