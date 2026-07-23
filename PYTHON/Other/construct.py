# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def display(self):
#         print("Name = ",self.name)
#         print("Age  = ",self.age)

# std=student("Rihan",21)
# # std.get_data("Rihan",12)
# std.display()

# write a pgm to implement inheritance a class teacher as a  result method and and 
# student has attandance method
# by the concept of inhertance make studnt object to access both methd

class teacher:
    def result(self,marks):
        self.marks=marks
        if self.marks>=45:
            print("pass")
        else:
            print("fail")

class student(teacher):
    def attendence(self,at):
        self.at=at
        if self.at>75:
            print("Eligible to exam")
        else:
            print("Not eligible to vote")    

s1=student()
s1.result(50)
s1.attendence(80)
