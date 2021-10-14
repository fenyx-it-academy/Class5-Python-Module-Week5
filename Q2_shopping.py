"""Define a class named ItemInfo with the following description:
item_code(Item Code), item(item name), price(Price of each item),
 qty(quantity in stock), discount(Discount percentage on the item), 
 net_price(Price after discount)

Methods :
A member method calculate_discount() to calculate discount as per the following rules:
-If qty <= 10 —> discount is 0
-If qty (11 to 20 inclusive) —> discount is 15
-If qty >= 20 —> discount is 20
-A constructor init method to assign the initial values for item_code to 0 and price,
qty, net_price and discount to null
-A function called buy() to allow user to enter values for item_code, item, price, qty.
-Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
-A function show_all() or similar name to allow user to view the content of all the data members."""






#We assign startup values to call after to calculate
class ItemInfo:  
    def __init__(self,item_code=0,item=None,price=None,qty=None,net_price=None,discount=None) : 
        self.item_code=item_code #Item Code
        self.item=item           #item name
        self.price=price         #Price of each item
        self.qty=qty             #Quantity in Stock
        self.net_price=net_price #Discount percentage on the item 
        self.discount=discount   #Price After Discount

    def calculate_discount(self): #This func calculate amount of discount
        if self.qty<=10:
           self.discount=0
        elif 11<=self.qty<=20:
           self.discount=15
        elif self.qty>=20:
           self.discount=20
        return self.discount

    def buy(self):               #This func generates net price of items
        self.item_code=int(input("Enter item code :"))
        self.item=input("Enter Item Name :")
        self.price=int(input("Enter price of item :"))
        self.qty=int(input("Enter quantity of items :"))
        self.calculate_discount()
        self.net_price=(self.price * self.qty-self.discount)
        return self.net_price

    def show_all(self):   #This will display the content of all the data members to user .
      print(f"""Item Code: {self.item_code}
Item Name: {self.item}
Price : {self.price}
Quantity : {self.qty}
Discount : {self.calculate_discount()}
Net Price : {self.net_price}""")


Ex=ItemInfo()
Ex.buy()
Ex.calculate_discount()
Ex.show_all()