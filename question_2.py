class ItemInfo:
    def __init__(self,item_code=0, item=None, price=None, qty=None, discount=None, net_price=None):
        self.item_code = item_code
        self.item = item
        self.price = price
        self.qty = qty
        self.discount = discount
        self.net_price = net_price

    def calculate_discount(self):
        if self.qty <= 10:
            self.discount = 1
        elif self.qty >=11 and self.qty <20:
           self.discount = 0.85
        else:
            self.discount = 0.8
        return self.discount
    def buy(self):
        self.item_code = input("Please enter code of item!: ")
        self.item = input("Please enter name of item!: ")
        self.price = float(input("Please enter price of item!: "))
        self.qty = int(input("Please enter quantity of item! "))
        self.calculate_discount()
        self.net_price = self.price * self.discount


    def show_all(self):
        print(f"Hello dear Customer :  \
You ordered {self.item_code} {self.item}. The price of product is {self.net_price} \
and quantity is {self.qty} ")

i = ItemInfo()
i.buy()
i.show_all()