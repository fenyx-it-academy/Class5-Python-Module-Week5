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

A=society("Happy Members",5,100,20000)
A.allocate_flat()
A.show_data()