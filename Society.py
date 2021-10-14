## Question 1:
"""Create the class `Society` with following information:

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
| <15000 | D Type      | """

class Society:
    """
    This class's name society and it store people and allocate flats 
    """
    def __init__(self,society_name,house_no,no_of_members,income):
        self.society_name = society_name
        self.house_no = house_no
        self.no_of_members = no_of_members
        self.income = income
    def allocate_flat(self):
        """
        This methot is allocate to flat according to income
        """
        if self.income >= 25000 : 
            self.flat = "A Type"
        elif self.income >= 20000 and self.income < 25000 :
            self.flat = "B Type"
        elif self.income >= 15000 and self.income < 20000 :
            self.flat = "C Type"
        else : 
            self.flat = "D Type"
    def show_data(self):
        print(f"Society name is {self.society_name} which is house number {self.house_no} . Number of members {self.no_of_members} and according to income ({self.income}) flat is {self.flat} ")

society_1 = Society("Trols",2,25,20000)

society_1.allocate_flat()
society_1.show_data()
    