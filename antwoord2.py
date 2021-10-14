## Question 2:
'''Define a class named `ItemInfo` with the following description:

`item_code`(Item Code), `item`(item name), `price`(Price of each item), 
    `qty`(quantity in stock), `discount`(Discount percentage on the item), 
    `net_price`(Price after discount)

**Methods :**
*	A member method `calculate_discount()` to calculate discount as per the 
following rules:
*	If `qty <= 10` —> discount is `0`
*	If `qty (11 to 20 inclusive)` —> discount is `15`
*	If `qty >= 20` —> discount is `20`
*	A constructor init method to assign the initial values for `item_code` to `0`
 and `price`, `qty`, `net_price` and `discount` to `null`
*	A function called `buy()` to allow user to enter values for `item_code`, 
`item`, `price`, `qty`. Then call function `calculate_discount()` to calculate the `discount` and `net_price`(price * qty - discount).
*	A function `show_all()` or similar name to allow user to view the content 
of all the data members.

'''


class ItemInfo:


    def __init__(self,):
        self.item_code = 0
        self.item = None
        self.price = None
        self.qty = None
        self.net_price = None
        self.discount = None
    
    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        elif 11 <= self.qty < 20:
            self.discount = 15
        elif self.qty >= 20:
            self.discount = 20
        dis_1 = self.price * self.qty * self.discount /100
        self.net_price = self.price * self.qty - dis_1
        return self.net_price

    def buy(self):
        self.item_code = int(input('Enter item code : '))
        self.item = input('Enter item name : ')
        self.price = int(input('Enter price : '))
        self.qty = int(input('Enter qty : '))
        self.calculate_discount()
        
    def show(self):
        self.buy()
        print(f'Code :{self.item_code}')
        print(f'name :{self.item}')
        print(f'Price :{self.price}')
        print(f'Qty :{self.qty}')
        print(f'Net Price :{self.net_price}')
        print(f'Discount  :{self.discount}%')
    
buy1 = ItemInfo()
print(buy1.show())