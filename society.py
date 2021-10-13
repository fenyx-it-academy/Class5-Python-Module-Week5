class Society:# I created the class Society
    def __init__(self,society_name,house_no,no_of_members,income):#An __init__ method to assign initial values
        self.society_name=society_name
        self.house_no=house_no
        self.no_of_members=no_of_members
        self.income=income
    
    def allocate_flat(self):#allocate_flat() to allocate flat according to income using the table
        if self.income>=25000:
            self.flat="A Type"
        elif self.income>=20000 and self.income<25000:
            self.flat="B Type"
        elif self.income>=15000 and self.income<20000:
            self.flat="C Type"
        elif self.income<15000:
            self.flat="D Type"

    def show_data(self):#show_data() to display the details of the entire class.
        return f"Society name:{self.society_name} \tHouse number:{self.house_no} \tNumbers of menbers:{self.no_of_members} \tIncome:{self.income} \tFlat Type:{self.flat}"

society1=Society("Rich",10,3,30000)# I Created one object for each flat type
society2=Society("Middel",20,4,21000)
society3=Society("Poor",23,5,12000)
society4=Society("Premiddel",17,4,18000)

society1.allocate_flat()
society2.allocate_flat()
society3.allocate_flat()
society4.allocate_flat()

print(society1.show_data())
print(society2.show_data())
print(society3.show_data())
print(society4.show_data())