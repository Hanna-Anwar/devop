class Book:

    def __init__(self,name,author,price):

        self.name = name

        self.author = author

        self.price = price

    
    def display_book(self):

        print(self.name,self.author,self.price)


    def __str__(self):

        return self.author

book_instance = Book("HarryPotter Series" ,"JK Rowling" ,"1200")

book_instance.display_book()

print(book_instance)
        