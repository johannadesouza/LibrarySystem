### Den här filen ska ha en klass som heter LibrarySystem.
### Klassen ska hantera böckerna i biblioteket och ha attribut som namn och en lista med böcker.
### Den ska kunna lägga till böcker, ta bort böcker, låna böcker, returnera böcker och kolla ifall att en bok är tillgänglig eller inte.
### I den här filen importerar vi klassen Book från book.py.
### Klassen hanterar en bok i taget.

from book import Book
import datetime as Datetime

class LibrarySystem:
    def __init__(self, name, books):
        self.name = name
        self.books = {} # Dictionary låter dig lagra data i par. Vilket gör att vi kan lagra böcker med deras titel som nyckel och sedan författare, utlåningsstatus mm som värde.

    # Lägger till en bok i biblioteket
    def addBook(self, title, author):
        if title in self.books:
            return f"Boken {title} finns redan i biblioteket."
        else:
            new_book = Book(title, author)
            self.books[title] = new_book # Lägger till ny bok i dict med titel som nyckel.
            return f"Boken {title} av {author} är nu tillagd i biblioteket."

    # Tar bort en bok från biblioteket
    def removeBook(self, title):
        try:
            del self.books[title]
            return f"Vi har tagit bort {title} från biblioteket."
        except KeyError:
            return f"Boken {title} finns inte i biblioteket."

    # Lånar ut en bok från biblioteket
    def borrowBook(self, title): 
        try:
            if title not in self.books:
                return f"Boken {title} finns inte i vårt bibliotek."
                
            book = self.books[title]
            if not book.is_borrowed: # Om boken inte är utlämnad
                book.mark_as_borrowed() # Lämna ut boken.
                return f"Boken {title} är nu utlånad."
            else: 
                return f"Boken {title} är redan utlånad."
        except KeyError:
            return f"Boken {title} finns inte i vårt bibliotek."


    # Lämnar tillbaka en bok till biblioteket
    def returnBook(self, title):
        try: 
            book = self.books[title]
            if book.is_borrowed:
                days_overdue = book.calculate_overdue_days(Datetime.datetime.now()) # Räkna ut hur många dagar boken är försenad.
                book.mark_as_returned() # Returnera boken.

                if days_overdue > 14: 
                    days_overdue = days_overdue - 14 # Om boken är lånad mer än 14 dagar är den försenad.
                    return f"Boken {title} är nu återlämnad. Du är {days_overdue} dagar försenad med att lämna tillbaka boken."
                else: 
                    return f"Boken {title} är nu återlämnad."
            else:
                return f"Boken {title} har redan återlämnats hos oss."
        except KeyError:
            return f"Boken {title} finns inte in vårt bibliotek."


    # Kollar ifall att en bok är tillgänglig eller inte
    def isBookAvailable(self, title):
        try:
            book = self.books[title]
            if book.is_borrowed:
                return f"Boken {title} går inte att låna"
            else: 
                return f"Boken {title} går att låna"
        except KeyError:
            return f"Boken {title} finns inte hos oss."

        

    # Visar alla böcker i biblioteket
    def displayAllBooks(self):
        if not self.books: # Om biblioteket är tomt
            return "Det finns inga böcker i biblioteket"
        
        book_list = ["Böcker i biblioteket: "]
        for title, book in self.books.items():
            status = "Utlånad" if book.is_borrowed else "Går att låna"
            book_list.append(f"{title} av {book.author} - {status}")
        return '\n'.join(book_list)

     

    # Visar alla böcker som är tillgängliga att låna i biblioteket
    def displayAvailableBooks(self):
        available_books = []

        for title, book in self.books.items():
            if not book.is_borrowed:
                available_books.append(title)

        if not available_books:
            return "Inga böcker finns att låna"
        else: 
            available_books_list = ["Böcker som finns att låna: "]
            for title in available_books:
                available_books_list.append(title)
            return available_books_list

    # Visar alla böcker som är utlånade i biblioteket, alltså inte tillgängliga att låna, samt hur länge de varit utlånade.
    def displayBorrowedBooks(self):
        borrowed_books = []

        print("Böcker som är utlånade:")
        for title, book in self.books.items():
            if book.is_borrowed:
                borrowed_days = book.calculate_overdue_days(Datetime.datetime.now())
                if borrowed_days > 14:
                    days_overdue = borrowed_days - 14
                    return f"{title} av {book.author} - Försenad med {days_overdue} dagar"
                else:
                    return f"{title} av {book.author} - Lånad i {borrowed_days} dagar"

            else:
                return "Inga böcker är utlånade"
