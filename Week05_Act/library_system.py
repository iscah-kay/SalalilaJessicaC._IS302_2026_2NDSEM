class Book_jcs:
    def __init__(self_jcs, title_jcs, author_jcs, year_jcs):
        self_jcs.title_jcs = title_jcs
        self_jcs.author_jcs = author_jcs
        self_jcs.year_jcs = year_jcs
    
    def display_book_jcs(self_jcs):
        print("Title:", self_jcs.title_jcs)
        print("Author:", self_jcs.author_jcs)
        print("Year:", self_jcs.year_jcs)
        print()

print("----- LIBRARY MANAGEMENT SYSTEM -----\n")

# Create three book objects
book1_jcs = Book_jcs("Python Programming", "John Smith", 2022)
book2_jcs = Book_jcs("Data Science Basics", "Sarah Johnson", 2021)
book3_jcs = Book_jcs("Web Development Guide", "Mike Davis", 2023)

# Display book information
print("Book 1:")
book1_jcs.display_book_jcs()

print("Book 2:")
book2_jcs.display_book_jcs()

print("Book 3:")
book3_jcs.display_book_jcs()
