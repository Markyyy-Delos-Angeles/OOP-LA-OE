
class BirthdayParty:
    def __init__(self, theme, special_d, secret_d):
        self.theme = theme
        self.special_d = special_d
        self.secret_d = secret_d
    
    def Allfoods(self):
        print(f"List of Foods Theme: {self.theme}\n")
        print(f"Special Dish: {self.special_d}\n")
        self._secret()
        print("================================================\n")

    def _secret(self):
        print(f"Secret Dish: {self.secret_d}")

theme1 = BirthdayParty("Toy Story", "Spaghetti", "Fried Chicken")
theme1.Allfoods()

theme2 = BirthdayParty("Avengers", "Cake", "Juice")
theme2.Allfoods()

theme3 = BirthdayParty("Harry Potter", "Fruits", "Wine")
theme3.Allfoods()