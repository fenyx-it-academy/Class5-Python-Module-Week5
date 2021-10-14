class Item_Info:

    def __init__(self ,item, item_code=0,price = None,qty=None,discount=None,net_price=None):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price

    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 0
        elif 11 <= self.qty <20:
            self.discount = self.price*0.15
        elif self.qty >= 20:
            self.discount = self.price*0.20

    def Buy(self):
        self.qty = int(input("How many do you want to buy?:"))
        self.item_code = input("Enter an item code:")
        self.price = int(input('enter the price:'))
        self.calculate_discount() 
        self.net_price = (self.price-self.discount)
        return self.net_price   


    def show_all(self):
        return f"Item name is {self.item},item code is {self.item_code},price is {self.price},quantity is {self.qty},discount is {self.discount},net price is {self.net_price}"
i = Item_Info('chocolade')
i.Buy()
#i.calculate_discount()
print(i.show_all())