class Library:
    def __init__(self,name,address,phone_number):
        self.name=name
        self.address=address
        self.phone_number=phone_number
        self.books=[]
    def book_taken(self,book):
        self.books.append(book)
    def book_returned(self,book):
        self.books.remove(book)
    def display(self):
            print(self.name,self.address,self.phone_number)
            print("books:")
            print(self.books)
obj=Library("Akku","kerala","678999655")
obj.book_taken("python")
obj.book_taken("java")
obj.book_taken("c++")
obj.display()
obj.book_returned("python")
obj.display()