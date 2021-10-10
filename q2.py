# Question 2:
# Define a class named `ItemInfo` with the following description:

# `item_code`(Item Code), `item`(item name), `price`(Price of each item), `qty`(quantity in stock), `discount`(Discount percentage on the item), `net_price`(Price after discount)

# **Methods :**
# *	A member method `calculate_discount()` to calculate discount as per the following rules:
# *	If `qty <= 10` —> discount is `0`
# *	If `qty (11 to 20 inclusive)` —> discount is `15`
# *	If `qty >= 20` —> discount is `20`
# *	A constructor init method to assign the initial values for `item_code` to `0` and `price`, `qty`, `net_price` and `discount` to `null`
# *	A function called `buy()` to allow user to enter values for `item_code`, `item`, `price`, `qty`. Then call function `calculate_discount()` to calculate the `discount` and `net_price`(price * qty - discount).
# *	A function `show_all()` or similar name to allow user to view the content of all the data members.

class ItemInfo:
    def __init__(self,item_code=0,item=None,price=None,qty=None,net_price=None,discount=None):
        self.item=item
        self.item_code=item_code
        self.price=price
        self.qty=qty
        self.discount=discount
        self.net_price=net_price
    def calculate_discount(self):
        if self.qty<=10:
            self.discount=0
        elif 20>=self.qty>11:
            self.discount=15
        else:
            self.discount=20
        return self.discount
    def buy(self):
        self.item=input('Item: ')
        self.item_code=input('Item Code: ')
        self.price=float(input('Price: '))
        self.qty=int(input('Quantity in stock: '))
        self.calculate_discount()
        self.net_price=self.price*((100-self.discount)/100)
    def show_all(self):
        print(f'Item code: {self.item_code} \nItem name: {self.item}\nPrice: {self.price}\nQuantity in Stock: {self.qty}\nDiscount:{self.calculate_discount()}\nNet Price:{self.net_price}')
pen = ItemInfo()
pen.buy()
pen.show_all()