class Society:
    def __init__(self,society_name,house_no,no_of_members,flat,income):
        self.society_name = society_name
        self.house_no = house_no
        self.no_of_members = no_of_members
        self.flat = flat
        self.income = income

    def allocate_flat(self):
        if self.income >=25.000:
            self.flat = "A type"
        elif self.income >=20.000 and self.income <25.000:
            self.flat = "B type"
        elif self.income >=15.000 and  self.income <20.000:
            self.flat = "C type"
        else:
            self.flat = "D type"

    def show_data(self):
        print("Society Name: ", self.society_name)
        print("House No: ", self.house_no)
        print("No of Members: ", self.no_of_members)
        print("Flat: ", self.flat)
        print("Income: ", self.income)

s = Society("Happy",1907,10,"x",18.000)
s.allocate_flat()
s.show_data()