from modules.library_item import LibraryItem

class Author():
    name = None
class Book(LibraryItem):
    def __init__(self,title,upc,subject,isbn,authors,dbs_number):
        LibraryItem.__init__(self,title,upc,subject)
        self.isbn = isbn
        self.authors = authors
        self.dbs_number = dbs_number
