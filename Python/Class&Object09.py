# class Car:
#     color = "Red"
#     brand = "Toyota"
# car1 = Car()
# print(car1.color)  # Output: Red
# print(car1.brand)  # Output: Toyota


# class Student:
#     name = "John"
#     age = 20
# student1 = Student()
# print(student1.name)  # Output: John
# print(student1.age)   # Output: 20


# class Student:
#     name = "John"
# student1 = Student()
# print(student1.name)  # Output: John 


# class on defind contructor
# class Student:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

# s1 = Student("Md Sabbir Hossain", 25)
# print(s1.name, s1.age) 

# s2 = Student("Md Rakib Hossain", 50)
# print(s2.name, s2.age)

# class and obejct attr
# class Student:
#     collefe

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
# s1 = Student("Md Sabbir hassan", 50)
# print(s1.name)

# ======= Encapsulation =======
# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance  # Private attribute

#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self, newBalnce):
#         self.__balance = newBalnce

# acc1 = BankAccount("Md Sabbir Hossain", 1000)
# acc1.set_balance(1500)
# print(acc1.name, acc1.get_balance())  # Output: 1500

#======== Inheritence ========
# class Employee:
#     start_class = "2 Pm"
#     end_class = "10 Pm"

#     def change_time(self, new_end_time):
#         self.end_time = new_end_time
    
# class Techer(Employee):
#     def __init__(self, subject):
#         self.subject = subject

# t1 = Techer("Math")
# t1.change_time("12 Pm")
# print(t1.end_class, t1.subject, t1.start_class)
