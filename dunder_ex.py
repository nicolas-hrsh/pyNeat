class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        # This defines what print(book) will show
        return f"Book: {self.title}, Pages: {self.pages}"
    
    def __add__(self, other):
        # This defines how adding two books works
        # We combine their pages and keep the title of the first book
        return Book(self.title, self.pages + other.pages)
    
    def __len__(self):
        # This defines what len(book) will return
        return self.pages

# Create two book objects
book1 = Book("Python Basics", 100)
book2 = Book("Advanced Python", 150)

print(book1)          # Calls book1.__str__()
print(len(book1))     # Calls book1.__len__()

combined = book1 + book2  # Calls book1.__add__(book2)
print(combined)       # Shows combined book info
print(len(combined))  # Number of pages in combined book
