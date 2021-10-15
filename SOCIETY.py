"""Create the class Society with following information:

society_name, house_no, no_of_members, flat, income

Methods :

An __init__ method to assign initial values of society_name, house_no, no_of_members, income
allocate_flat() to allocate flat according to income using the below table -> according to income, it will decide to flat type
show_data() to display the details of the entire class.
Create one object for each flat type, for each object call allocate_flat() and show_data()
Income           	Flat
>=25000	            A Type
>=20000 and <25000	B Type
>=15000 and <20000	C Type
<15000	            D Type
"""




class society:
        def __init__(self,society_name,house_no,no_of_members,income):
                self.society_name=society_name
                self.house_no=house_no
                self.no_of_members=no_of_members
                self.income=income
        
        def allocate_flat(self):
                if self.income >= 25000:
                        self.flat = 'A Type'
                elif self.income >= 20000:
                        self.flat = 'B Type'
                elif self.income >= 15000:
                        self.flat = 'C Type'
                else:
                        self.flat = 'D Type'
        def show_data(self):
            print(f"Society Name: {self.society_name},House No: {self.house_no},No of Members: {self.no_of_members},Income: {self.income},Flat: {self.flat}")


S=society("X APARTMENTS",30,4,15000)
S.allocate_flat()
S.show_data()