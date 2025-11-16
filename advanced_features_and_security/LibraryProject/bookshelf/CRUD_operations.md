#Creating a new object
    >>> new_book = Book(title = '1984', author = 'George Orwell', published_year = 1949) 
    #The error generated was as below 
        Traceback (most recent call last):
    File "<console>", line 1, in <module>
    File "/home/piezo/.local/share/virtualenvs/Introduction_to_Django-1GJirNNL/lib/python3.11/site-packages/django/db/models/     
        base.py", line 569, in __init__
        raise TypeError(
    TypeError: Book() got unexpected keyword arguments: 'published_year'

    >>> new_book = Book(title = '1984', author = 'George Orwell', publication_year = 1949) 
    >>> new_book.save()


#Retrieving objects
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

#Updating objects
    >>> new_book(title = 'Nineteen Eighty-Four') #This was an error at first
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    TypeError: 'Book' object is not callable

    >>> new_book.title = 'Nineteen Eighty-Four' #no output was given meaning that the update was done successfully
    >>> new_book.title #Upon printing the newly updated title was shown
    'Nineteen Eighty-Four'
    >>> new_book.save() #I later on saved the update done


#Deleting objects
    >>> new_book.delete()
    (0, {'bookshelf.Book': 0})
    >>> 
