Create:
 At first I had run the following command wich eturned an error as specified below

Book.object.create(
    title = '1984', 
    author = 'George Orwell', 
    published_year = 1949
)

    >>> new_book = Book(title = '1984', author = 'George Orwell', published_year = 1949) 
The error generated was as below 
        Traceback (most recent call last):
    File "<console>", line 1, in <module>
    File "/home/piezo/.local/share/virtualenvs/Introduction_to_Django-1GJirNNL/lib/python3.11/site-packages/django/db/models/     
        base.py", line 569, in __init__
        raise TypeError(
    TypeError: Book() got unexpected keyword arguments: 'published_year'

I realized that there was an error and corrected it and run it
    >>> new_book = Book(title = '1984', author = 'George Orwell', publication_year = 1949) 

Another option to take
Book.object.create(
    title = '1984', 
    author = 'George Orwell', 
    published_year = 1949
)

The command ran successfully!!!!!!!!!!!!!!!!!!!!!!!!!
