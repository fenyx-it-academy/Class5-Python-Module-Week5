# Question 1:
# Create the class `Society` with following information:

# `society_name`, `house_no`, `no_of_members`, `flat`, `income`

# **Methods :**

# *	 An `__init__` method to assign initial values of `society_name`, `house_no`, `no_of_members`, `income`
# *	`allocate_flat()` to allocate flat according to income using the below table -> according to income, it will decide to flat type
# *	`show_data()` to display the details of the entire class.
# *   Create one object for each flat type, for each object call `allocate_flat()` and `show_data()`

# | Income        | Flat           | 
# | ------------- |:-------------:| 
# | >=25000     | A Type | 
# | >=20000 and <25000     | B Type      | 
# | >=15000 and <20000 | C Type      |
# | <15000 | D Type      |

class Society:
    def __init__(self,society_name,house_no,no_of_members,income):
        self.society_name=society_name
        self.house_no=house_no
        self.no_of_members=no_of_members
        self.income=income
    def allocate_flat(self):
        if self.income>=25000:
            flat='A Type'
        elif 25000>self.income>=20000:
            flat='B Type'
        elif 20000>self.income>=15000:
            flat='C Type'
        else:
            flat='D Type'
        return flat
    def show_data(self):
        print(f'Society name: {self.society_name} \nHouse no: {self.house_no}\nNo of Members: {self.no_of_members}\nIncome: {self.income}\nFlat:{self.allocate_flat()}')
society_name1=Society('Test',25,6,22500)
society_name1.show_data()
society_name2=Society('Test2',12,4,16000)
society_name2.show_data()