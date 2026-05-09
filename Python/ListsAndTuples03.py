# lists are mutable, meaning that we can change their contents after they have been created. We can add, remove, or modify elements in a list.


student = ["Alice", 20, "Computer Science"]
print(student)
student[1] = 21  # Modifying the age
print(student)

# tuples are immutable, meaning that once they are created, their contents cannot be changed. We cannot add, remove, or modify elements in a tuple.

person = ("Bob", 30, "Engineer")
print(person)
