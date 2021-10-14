class Society:

    def __init__(self,society_name,house_no,no_fo_members,income):
        self.society_name = society_name
        self.house_no = house_no
        self.no_fo_members = no_fo_members
        self.income = income

    def allocate_flat(self):
        if self.income >= 25000:
            return "flat A"
        elif 20000 <= self.income < 25000:
            return "flat B"
        elif 15000 <= self.income < 20000:
            return "flat C"
        else:
            return "flat D"

    def show_data(self):
        print(f"Society name is {self.society_name},house no is {self.house_no}, number of family members are {self.no_fo_members}, income is {self.income}")

family_1 = Society("aydin",24,5,10000)
family_2 = Society("cetin", 26,4,16000)
family_3 = Society("cakir", 22,3,21000)
family_4 = Society("kara",21,3,25000)

print(family_1.allocate_flat())
family_1.show_data()