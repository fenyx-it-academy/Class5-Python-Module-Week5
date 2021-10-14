'''Question 1:
Create the class `Society` with following information:

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

    def __init__(self,society_name, house_no, no_of_members, income):

        self.society_name=society_name
        self.house_no=house_no
        self.no_of_members=no_of_members
        self.income=income

    def allocate_flat(self):

        if self.income >=25000:
            return 'A type'
        elif self.income >=20000 and self.income< 25000:
            return 'B type'
        elif self.income >=15000 and self.income<20000:
            return 'C type'
        else: 
            return 'D type'

    def show_data(self):
        print("Society Name :", self.society_name)
        print("House No :", self.house_no)
        print("No of Memmbers :", self.no_of_members)
        print("Income :", self.income)
        print("Allocate Flat :", self.allocate_flat())







Society1=Society("Internet Society",24,234,27000)
Society2=Society("Language Society",48,99,22000)
Society3=Society("Information Technology Society",22,3000,17590)
Society4=Society("Gym Society",9,45,7766)

Society1.show_data()
Society2.show_data()
Society3.show_data()
Society4.show_data()






    
