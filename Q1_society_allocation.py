"""Create the class Society with following information:
society_name, house_no, no_of_members, flat, income
Methods :
1)An __init__ method to assign initial values of society_name, house_no, no_of_members, income
2)allocate_flat() to allocate flat according to income using the below table -> according to income, 
it will decide to flat type
3)show_data() to display the details of the entire class.
4)Create one object for each flat type, for each object call allocate_flat() and show_data()
Income	            Flat
>=25000             A Type
>=20000 and <25000  B Type
>=15000 and <20000  C Type  
<15000	            D Type"""

class Society:       #We define initial values of society_name, house_no, no_of_members, income
    def __init__(self,society_name, house_no, no_of_members, income):
       self.society_name = society_name
       self.house_no=house_no
       self.no_of_members=no_of_members
       self.income=income

    def allocate_flat(self):       #We define allocation types,according to income
        if self.income>=25000:
            self.flat='A Type'
        elif 20000<=self.income <25000:
            self.flat='B Type'
        elif 15000<=self.income<20000:
            self.flat='C Type'
        elif self.income<15000 :
            self.flat='D Type'
        return self.flat

    def show_data(self):      #We display details of entire class
        print(f"""
Society Name:{self.society_name} 
House_No : {self.house_no} 
Number of Members: {self.no_of_members}
Income : {self.income}
Allocation : {self.allocate_flat()}""",end="\n  ---->")

Ex_1=Society("Red",4,6,15000)
Ex_2=Society("Teal",3,5,40000)
Ex_3=Society("Black",1,1,8000)
Ex_4=Society("White",11,2,23000)
Ex_1.show_data()
Ex_2.show_data()
Ex_3.show_data()
Ex_4.show_data()

