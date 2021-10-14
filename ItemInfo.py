"""Define a class named `ItemInfo` with the following description:

`item_code`(Item Code), `item`(item name), `price`(Price of each item), `qty`(quantity in stock),
 `discount`(Discount percentage on the item), `net_price`(Price after discount)

**Methods :**
*	A member method `calculate_discount()` to calculate discount as per the following rules:
*	If `qty <= 10` —> discount is `0`
*	If `qty (11 to 20 inclusive)` —> discount is `15`
*	If `qty >= 20` —> discount is `20`
*	A constructor init method to assign the initial values for `item_code` to `0` and `price`, `qty`,
    `net_price` and `discount` to `null`
*	A function called `buy()` to allow user to enter values for `item_code`, `item`, `price`, `qty`. 
Then call function `calculate_discount()` to calculate the `discount` and `net_price`(price * qty - discount).
*	A function `show_all()` or similar name to allow user to view the content of all the data members."""

class ItemInfo:
    def __init__(self,item_code=0,qty= 0):
        """
        price = price of each item
        qty = quantity in stock
        discount = discount percentage on the item
        net_price = price after discount"""
        self.item_code = item_code
        self.qty = qty
    def calculate_discount(self):
        """
        If `qty <= 10` —> discount is `0`
        If `qty (11 to 20 inclusive)` —> discount is `15`
        If `qty >= 20` —> discount is `20` """
    
        if self.qty <= 10 :
            self.discount = 0
        elif self.qty  >= 11 and self.qty <= 20 : 
            self.discount = self.price * 0.15 * self.qty
        elif self.qty >= 20 : 
            self.discount = self.price * 0.20 * self.qty
        self.net_price = self.price*self.qty-self.discount
    def buy (self,item_code,item,price):
        """A function called `buy()` to allow user to enter values for `item_code`, `item`, `price`, `qty`. 
        """
        self.item_code = item_code
        self.item = item
        self.price = price
        self.calculate_discount()
    def show_all (self):
        print(f"item code : {self.item_code}\nitem name : {self.item}\nprice : {self.price}\nquantity in stock : {self.qty}\ndiscount : {self.discount}\nNET PRICE {self.net_price} ")

sweet = ItemInfo(212521,25)
buy_itemcode = int(input("itemcode : "))
buy_item = input("item name : ")
buy_price = int(input("Price : "))
sweet.buy(buy_itemcode,buy_item,buy_price)
sweet.show_all()