Updating:
The commands and outpits below give a summary of what I did 
    >>> new_book(title = 'Nineteen Eighty-Four') #This was an error at first
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
    TypeError: 'Book' object is not callable

    >>> new_book.title = 'Nineteen Eighty-Four' #no output was given meaning that the update was done successfully
    >>> new_book.title #Upon printing the newly updated title was shown
    'Nineteen Eighty-Four'
    >>> new_book.save() #I later on saved the update done