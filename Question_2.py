'''## Question 2:
Define a class named `ItemInfo` with the following description:

`item_code`(Item Code), `item`(item name), `price`(Price of each item), `qty`(quantity in stock), `discount`(Discount percentage on the item), `net_price`(Price after discount)

**Methods :**
*	A member method `calculate_discount()` to calculate discount as per the following rules:
*	If `qty <= 10` —> discount is `0`
*	If `qty (11 to 20 inclusive)` —> discount is `15`
*	If `qty >= 20` —> discount is `20`
*	A constructor init method to assign the initial values for `item_code` to `0` and `price`, `qty`, `net_price` and `discount` to `null`
*	A function called `buy()` to allow user to enter values for `item_code`, `item`, `price`, `qty`. Then call function `calculate_discount()` to calculate the `discount` and `net_price`(price * qty - discount).
*	A function `show_all()` or similar name to allow user to view the content of all the data members.

'''

class ItemInfo:
    
    def __init__(self, item_code = 0, item = None, price = None, qty = None, discount = None, net_price= None ):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price
    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        elif 20>=self.qty >= 10:
            self.discount = 15
        elif self.qty >= 20:
            self.discount = 20
        return self.discount
    def buy(self):
        self.item_code=input("item code: ")
        self.item = input("item: ")
        self.price = int(input("price: "))
        self.qty = float(input("qty: "))
        self.calculate_discount()
        self.net_price = self.price * self.qty - self.discount

    def show_all(self):
        return print(f"item code:{self.item_code} \n item: {self.item} \n price: {self.price} \n qty: {self.qty } \n discount:{self.discount} \n net price:{self.net_price} ")
shirt = ItemInfo()
shirt.buy()
shirt.show_all()
