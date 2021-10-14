class Employee:
        new_id=1
        def __init__(self):
                self.name=input("enter Employee name:")
                Employee.new_id+=1
                self.new_id=Employee.new_id
                self.id=self.new_id
        def say_id(self):
                return (f"{self.name}'s id is {self.id}")

e1=Employee()
e2=Employee()
print(e1.id)
print(e2.id)
print(e1.say_id())
print(e2.say_id())