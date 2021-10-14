class ItemInfo:
        def __init__(self):
                self.item_code=0
                self.price=None
                self.qty=None
                self.discount=None
                self.net_price=None
                self.buy()
        
        def buy(self):
                self.item_code = int(input("Enter item code: "))
                self.item = input("Enter item name: ")
                self.price = float(input("Enter the price: "))
                self.qty = int(input("Enter qty: "))
                self.calculate_discount()
        
        def calculate_discount(self):
                if self.qty <= 10:
                        self.discount=0
                        self.net_price=self.price * self.qty - self.discount
                elif 10 <= self.qty < 20:
                        self.discount=15
                        self.net_price=self.price * self.qty - self.discount
                elif 20 <= self.qty :
                        self.discount=20
                self.show_all()
                        
        def show_all(self):
                print(f"Item Code: {self.item_code},Item Name: {self.item},Price:{self.price},Item Quantity: {self.qty},Discount: {self.discount},Net Price: {self.price * self.qty - self.discount}")

item = ItemInfo()

