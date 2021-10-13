class ItemInfo:#I defined a class named ItemInfo
    def __init__(self,item_code=0,item=0,price=0,qty=0,discount=0,netprice=0):
        self.item_code=item_code
        self.item=item
        self.price=price
        self.qty=qty
        self.discount=discount
        self.netprice=netprice
    
    def calculate_discount(self):#I defined a method to calculate discount as per the following rules:
        if self.qty<=10:
            self.discount=0
        elif 11<self.qty<20:
            self.discount=15
        elif self.qty>=20:
            self.discount=20
        return self.discount
    
    def buy(self):#This method calculate the discount of the item
        self.item_code=input("Plese enter item code : ")
        self.item=input("Please enter the name of item: ")
        self.price=int(input(f"Please enter the price of the {self.item}: "))
        self.qty=int(input(f"Please enter the quantity of the{self.item}: "))
        self.discount=self.calculate_discount()
        self.netprice=(self.price*self.qty)-self.discount

    def show_all(self):# i defined a method that allows to the user to view the content of all the data members.
        return f"Item code:{self.item_code} \nItem:{self.item}\nItem Price:{self.price}\nItem quantity:{self.qty}\nItem discount:{self.discount}\nItem Net Price:{self.netprice}"

item1=ItemInfo()
item1.buy()
print(item1.show_all())