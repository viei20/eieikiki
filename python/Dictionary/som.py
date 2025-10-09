books = []
def add_book(books, isbn, title, author, copies):
    book = {
        'isbn': isbn,
        'title': title,
        'author': author,
        'copies': copies,
    }
    for i in books:
        if i['isbn'] ==isbn:
            print("Error")
            return
    books.append(book)
     
def search_book(books,keyword):
    have = False
    for i in books:
        if keyword in i['title'] or  keyword in i['author']:
            print(f"ISBN : {i['isbn']}")
            print(f"TITLE: {i['title']}")
            print(f"AUTHOR : {i['author']}")
            print(f"COPIES : {i['copies']}")
            print(f"---------------------------")
            have = True
    if have == False:
        print("Don't have Book.")
    
def show_book(books):
    for i in books:
        print(f"ISBN : {i['isbn']}")
        print(f"TITLE: {i['title']}")
        print(f"AUTHOR : {i['author']}")
        print(f"COPIES : {i['copies']}")
        print(f"---------------------------")
    
add_book(books, '001', 'Python Crash Course', 'Eric Matthes', 3)
add_book(books, '001', 'Python Crash Course', 'Eric Matthes', 3)
add_book(books, '002', 'Clean Code', 'Robert Martin', 2) 
add_book(books, '003', 'The Pragmatic Programmer', 'Hunt & Thomas', 2) 
add_book(books, '004', 'Design Patterns', 'Gang of Four', 1) 
add_book(books, '005', 'Introduction to Algorithms', 'Cormen et al.', 2) 
add_book(books, '006', 'Code Complete', 'Steve McConnell', 3) 
add_book(books, '007', 'Refactoring', 'Martin Fowler', 2)
# search_book(books, 'Code')
# show_book(books)
