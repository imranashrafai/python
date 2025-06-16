print("======================== Library Program ========================")


class Library:
    def __init__(self):
        self.nbook = 0
        self.book = []

    def addBooks(self, books):
        self.book.append(books)
        self.nbook = len(self.book)

    def show(self):
        print(f"Library has {self.nbook} books and books are:")
        for i, bk in enumerate(self.book):
            print(i + 1, bk)


li = Library()
li.addBooks("Imran Ashraf Chicken Recipies")
li.addBooks("Imran Ashraf Fish Recipies")
li.addBooks("Imran Ashraf Juice Recipies")
li.show()
