'''
## Question 1:
Create the class `Society` with following information:

`society_name`, `house_no`, `no_of_members`, `flat`, `income`

**Methods :**

*	 An `__init__` method to assign initial values of `society_name`, `house_no`, `no_of_members`, `income`
*	`allocate_flat()` to allocate flat according to income using the below table -> according to income,
     it will decide to flat type
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
    def __init__(self,society_name,house_no,no_of_members,income):
        self.society_name = society_name
        self.house_no = house_no
        self.no_of_members = no_of_members
        self.income = income

    def allocate_flat(self):
        self.flat = ['A Type','B Type','C Type','D Type']
        if self.income >= 25000:
            print(self.flat[0])
        elif 20000 <= self.income < 25000:
            print(self.flat[1])
        elif 15000 <= self.income < 20000:
            print(self.flat[2])
        elif self.income < 15000:
            print(self.flat[3])
        print('------------------------------')
    def show_data(self):
        print(f'society name is : {self.society_name}')
        print(f'house number is : {self.house_no}')
        print(f'no of members is : {self.no_of_members}')
        print(f'income is : {self.income}')
    
    def show(self):
        self.show_data()
        self.allocate_flat()
    
society1 = Society("aaa",11,123,35000)
society1.show()

society2 = Society("bbb",12,234,22000)
society2.show()

society3 = Society("ccc",13,345,18000)
society3.show()

society4 = Society("ddd",14,456,14000)
society4.show()
