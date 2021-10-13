class Employee:#I defined the Employee class with an __init__() method
    new_id=1 #I defined a class variable new_id and set it equal to 1
    def __init__(self):
        
        self.id=Employee.new_id #I defined self.id and it is equal to the class variable new_id
        Employee.new_id+=1 #increment new_id by 1

    def say_id(self):#I defined a say_id() method
        return f"My id is:{self.id}" #I wrote the output
e1=Employee() # I defined the variable e1 and e2 and I setted them to an instance of Employee
e2=Employee()
print(e1.say_id())
print(e2.say_id())