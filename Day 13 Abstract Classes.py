class MyBook(Book):
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display(self):
        print("Title: "+ title)
        print("Author: "+ author)
        print("Price:",price)
