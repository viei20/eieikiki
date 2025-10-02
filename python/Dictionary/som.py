books = []
def add_book(books, isbn, title, author, copies):
    book = {
        'isbn': isbn,
        'title': title,
        'author': author,
        'copies': copies,
    }
    books.append(book)
    # for  book in books:
    #     if book.values(isbn) ==  book.value(isbn):
    #         print("Error")
    # if book['isbn'] == book['isbn']:
    #     print("Error")

def search_book(books,keyword):
    find = keyword
    if find in books.values():
        print(book)


add_book(books, '001', 'Python Crash Course', 'Eric Matthes', 3)
search_book(books, 'Eric Matthes')
# add_book(books, '001', 'Python Crash Course', 'Eric Matthes', 3)
# add_book(books, '002', 'Clean Code', 'Robert Martin', 2) 
# add_book(books, '003', 'The Pragmatic Programmer', 'Hunt & Thomas', 2) 
# add_book(books, '004', 'Design Patterns', 'Gang of Four', 1) 
# add_book(books, '005', 'Introduction to Algorithms', 'Cormen et al.', 2) 
# add_book(books, '006', 'Code Complete', 'Steve McConnell', 3) 
# add_book(books, '007', 'Refactoring', 'Martin Fowler', 2)
