class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def __str__(self):
        return f"This car is a {self.brand}"
    
him = Car("Ford")
print(him)
print(him)
del him
print(him)