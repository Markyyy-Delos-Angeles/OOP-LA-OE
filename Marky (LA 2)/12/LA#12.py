class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describeToy(self):
        print(f"The Model is {self.name} lego toy comprises of 730 places and costs {self.price}")

class Play(Toy):
    def __init__(self, name, price):
        super.__init__(name, price)

him = Toy("Stitch", "£59.99")
him.describeToy()