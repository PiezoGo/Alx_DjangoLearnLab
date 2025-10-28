Retrieving values:

after creatinng the object called new_book and saving it using the commands below
    >>> new_book = Book(title = '1984', author = 'George Orwell', publication_year = 1949)
    >>> new_book.save()
    

I tried retrieving that very book using the following commands
    >>> books = Book.objects.all()
    >>> print(books)
    >>> print(new_book)
    >>> new_book.title
    >>> new_book.author
    >>> new_book.publication_year


Here are the commands and their corresponding outputs
    >>> print(books)
    <QuerySet [<Book: Book object (1)>]>
    >>> print(new_book)
    Book object (1)
    >>> new_book.title
    '1984'
    >>> new_book.author
    'George Orwell'
    >>> new_book.publication_year
    1949

I was successfull in retrieving the object that I created!!