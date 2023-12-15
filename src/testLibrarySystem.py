
### - Importera unittest till din fil och skapa en class vid namn **TestLibrarySystem** som ärver från unittest.TestCase,
### och som testar respektive metod från din **LibrarySystem** class.

import unittest
from library_system import LibrarySystem
import datetime as datetime

class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        print("Test 1")
        # Skapa en instans av LibrarySystem för varje testfall
        self.library = LibrarySystem("Test Library", {})

    def test_addBook(self):
        # Testa att lägga till en bok
        print("Test 2")
        self.library.addBook("The Catcher in the Rye", "J.D. Salinger")
        self.assertTrue("The Catcher in the Rye" in self.library.books)


    def test_removeBook(self):
        print("Test 3")
        # Testa att ta bort en bok
        self.library.addBook("1984", "George Orwell")
        self.library.removeBook("1984")
        self.assertFalse("1984" in self.library.books)
        

    def test_borrowBook(self):
        print("Test 4")
        # Testa att låna en bok
        self.library.addBook("Pride and Prejudice", "Jane Austen")
        self.library.borrowBook("Pride and Prejudice")
        self.assertTrue(self.library.books["Pride and Prejudice"].is_borrowed)

    def test_returnBook(self):
        print("Test 5")
        # Testa att returnera en bok
        self.library.addBook("To Kill a Mockingbird", "Harper Lee")
        self.library.borrowBook("To Kill a Mockingbird")
        result = self.library.returnBook("To Kill a Mockingbird")
        self.assertIn("To Kill a Mockingbird", result) # Kontrollera att bokens titel finns i resultatet
        self.assertFalse(self.library.books["To Kill a Mockingbird"].is_borrowed) # Kontrollera att boken inte är utlämnad, vi vill att den ska vara False

    def test_returnBook_overdue(self):
        print("Test 6")
        # Låna boken och sätt datumet till fler än 14 dagar sedan
        self.library.addBook("Hallå", "Jalle")
        self.library.borrowBook("Hallå")
        self.twenty_days = datetime.datetime.now() - datetime.timedelta(days=20)
        self.library.books["Hallå"].borrowed_date = self.twenty_days
        #Returnera boken och kontrollera om den är försenad 
        expected_message = f"Boken Hallå är nu återlämnad. Du är 6 dagar försenad med att lämna tillbaka boken."
        actual_message = self.library.returnBook(f"Hallå")
        self.assertEqual(expected_message, actual_message)

    def test_isBookAvailable(self):
        print("Test 7")
        # Testa att kolla ifall att en bok är tillgänglig
        self.library.addBook("The Great Gatsby", "F. Scott Fitzgerald")
        result = self.library.isBookAvailable("The Great Gatsby")
        self.assertEqual(result, f"Boken The Great Gatsby går att låna")
    
    def test_isBookAvailable_notAvailable(self):
        print("Test 8")
        # Testa att kolla ifall att en bok inte är tillgänglig
        self.library.addBook("The Great Gatsby", "F. Scott Fitzgerald")
        self.library.borrowBook("The Great Gatsby")
        result = self.library.isBookAvailable("The Great Gatsby")
        self.assertEqual(result, f"Boken The Great Gatsby går inte att låna")

    def test_displayAvailableBooks(self):
        print("Test 9")
        # Testa att visa alla tillgängliga böcker
        self.library.addBook("The Great Gatsby", "F. Scott Fitzgerald")
        self.library.addBook("The Catcher in the Rye", "J.D. Salinger")
        self.library.addBook("To Kill a Mockingbird", "Harper Lee")
        self.library.borrowBook("The Great Gatsby")
        self.library.borrowBook("To Kill a Mockingbird")
        result = self.library.displayAvailableBooks()
        
        expected_result = ['Böcker som finns att låna: ', 'The Catcher in the Rye']
        self.assertEqual(result, expected_result)
    
    def test_displayBorrowedBooks(self):
        print("Test 10")
        # Testa att visa alla utlånade böcker
        self.library.addBook("The Great Gatsby", "F. Scott Fitzgerald")
        self.library.addBook("The Catcher in the Rye", "J.D. Salinger")
        self.library.addBook("To Kill a Mockingbird", "Harper Lee")
        self.library.borrowBook("The Great Gatsby")
        result = self.library.displayBorrowedBooks()
        self.assertEqual(result, 'The Great Gatsby av F. Scott Fitzgerald - Lånad i 0 dagar')

## Det här testet funkar ju då vi bara kollar en bok som utlånad. Men skulle vi långa flere böcker så skulle det inte funka. 
## Vi måste då skapa en lista med alla utlånade böcker och kolla ifall att boken vi vill kolla finns i den listan.

if __name__ == '__main__':
    unittest.main()