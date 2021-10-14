'''
Define a class named `ItemInfo` with the following description:

`item_code`(Item Code), `item`(item name), `price`(Price of each item), `qty`(quantity in stock), 
`discount`(Discount percentage on the item), `net_price`(Price after discount)

**Methods :**
*	A member method `calculate_discount()` to calculate discount as per the following rules:
*	If `qty <= 10` —> discount is `0`
*	If `qty (11 to 20 inclusive)` —> discount is `15`
*	If `qty >= 20` —> discount is `20`
*	A constructor init method to assign the initial values for 
`item_code` to `0` and `price`, `qty`, `net_price` and `discount` to `null`
*	A function called `buy()` to allow user to enter values for`item_code`, `item`, `price`, `qty`. 
 Then call function `calculate_discount()` to calculate the `discount` and `net_price`(price * qty - discount).
*	A function `show_all()` or similar name to allow user to view the content of all the data members.

'''
class ItemInfo:
    
    def __init__(self,item_code, item_name, price, qty, discount, net_price ):

        self.item_code=item_code
        self.item_name=item_name
        self.price=price
        self.qty=qty
        self.discount=discount
        self.net_price=net_price

    def Buy(self): 
        
        self.item_code=input("Enter Item Code : ") 
        self.item_name=input("Enter Item Name : ")
        self.price=float(input("Enter Price : ")) 
        self.qty=int(input("Enter Quantity : "))

    def calculate_discount(self):


        if self.qty <= 10:

            self.discount=0
            #return self.discount

        elif self.qty>11 and self.qty<20:

            self.discount=15
            #return self.discount

        else:
            self.discount=20
            #return self.discount
        
        self.net_price= (self.price*self.qty - self.discount) 
        self.discount

    def __init__(self,item_code=None,price=None,qtr=None,discount=None,net_price=None):

        self.item_code=item_code
        self.price=price
        self.qty=qtr
        self.discount=discount
        self.net_price=net_price

    def Show_all(self):

        print("Item Code : ", self.item_code)
        print("Item Name : ", self.item_name)
        print("Item Price : ", self.price)
        print("Item Quantity : ", self.qty)
        print("Item Discount : ", self.discount)
        print("Item Net Price : ", self.net_price)
    


Item1=ItemInfo()
Item1.Buy()
Item1.calculate_discount()
Item1.Show_all()

