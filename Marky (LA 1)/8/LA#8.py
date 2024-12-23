class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Teen Class", "IDangs")

print("First Book Title and Author: ", book1.title, book1.author)

book1.author = "Blue Maiden"
del book1.author

book2 = Book("He's Into Her", "Maxinejiji")
print("Second Book Title and Author: ", book2.title, book2.author)