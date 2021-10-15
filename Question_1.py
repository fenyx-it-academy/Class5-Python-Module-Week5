'''Create the class `Society` with following information:

`society_name`, `house_no`, `no_of_members`, `flat`, `income`

**Methods :**

*	 An `__init__` method to assign initial values of `society_name`, `house_no`, `no_of_members`, `income`
*	`allocate_flat()` to allocate flat according to income using the below table -> according to income, it will decide to flat type
*	`show_data()` to display the details of the entire class.
*   Create one object for each flat type, for each object call `allocate_flat()` and `show_data()`

| Income        | Flat           | 
| ------------- |:-------------:| 
| >=25000     | A Type | 
| >=20000 and <25000     | B Type      | 
| >=15000 and <20000 | C Type      |
| <15000 | D Type      |
'''


class Society:
    
    def __init__(self, society_name, house_no, no_of_members, income):
        self.society_name = society_name
        self.house_no = house_no
        self.no_of_members = no_of_members
        self.income = income
    def allocate_flat(self):
        if self.income >= 25000:
            self.flat = "A Type"
        if 25000 >= self.income >= 20000:
            self.flat = "B Type"
        if 20000 >= self.income >= 15000:
            self.flatflat = "C Type"
        if self.income < 15000:
            self.flat = "D Type"
        return self.flat
    def show_data(self):
        print(f"the society name is :{self.society_name}, the income is : {self.income}, the flat type is :{self.flat} , the house no is :{self.house_no}")

s1 = Society("s1", 1, 3, 30000)
s2 = Society("s2", 2, 2, 22000)
s3 = Society("s3", 3, 3, 18000)
s4 = Society("s4", 4, 4, 14000)
Society.show_data(s1)