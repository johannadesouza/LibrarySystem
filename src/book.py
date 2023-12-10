### I den här filen så skapar vi en klass som heter Book.
### Klassen hanterar en bok i taget och kollar och hanterar bokens status.

import datetime

class Book:
    def __init__(self, title, author): # Konstruktorn körs när vi skapar en ny instans av klassen.
        self.title = title
        self.author = author
        self.is_borrowed = False # Vi sätter is_borrowed till False som default. Detta betyder att boken inte är utlämnad.
        self.borrowed_date = None # Vi sätter borrowed_date till None som default. Detta betyder att boken inte är utlämnad, därav inget datum för när boken lånades ut.

   # Markera en bok som utlånad
    def mark_as_borrowed(self): 
        self.is_borrowed = True # Vi sätter is_borrowed till True. Detta betyder att boken är utlämnad.
        self.borrowed_date = datetime.datetime.now() # Vi sätter borrowed_date till dagens datum. Detta betyder att boken är utlämnad och vi har ett datum för när boken lånades ut.


   # Markera en bok som återlämnad
    def mark_as_returned(self): 
        self.is_borrowed = False # Vi sätter is_borrowed till False. Detta betyder att att boken nu är tillbaka och inte längre utlämnad.
        self.borrowed_date = None # Vi sätter borrowed_date till None. Detta betyder att boken nu är tillbaka och vi inte längre har ett datum för när boken lånades ut.

   # Returnera information om boken 
    def get_info(self):
        return {
            "title": self.title,
            "author": self.author,
            "is_borrowed": self.is_borrowed
        }

    # Räkna ut hur många dagar en bok är försenad
    def calculate_overdue_days(self, return_date):
        if self.borrowed_date:
            days_overdue = (return_date - self.borrowed_date).days
            return days_overdue
        return 0
    
