import re
from library_system import LibrarySystem

### Här skapar vi ett tomt bibliotek som heter Mode.
### När vi kör filen, kan vi navigera i vårt bibliotek och göra olika saker. 
### Vi kan som lånetagare 

is_running = True
library = LibrarySystem("danskarna", {})

while is_running: 
    print("\nVälkommen till vårt biblioteksprogram!\n"
          "Hur vill du logga in?:\n"
            "1. Logga in som bibliotekarie\n"
            "2. Logga in som låntagare\n"
            "3. Avsluta programmet\n")
    try:
        choice = input("Ange ditt val: ")

        if choice == "1":
            print("Du är nu inloggad som bibliotekarie.")
            while True:
                print("\nVad vill du göra?:\n"
                    "1. Lägg till en bok\n"
                    "2. Ta bort en bok\n"
                    "3. Visa alla böcker\n"
                    "4. Visa tillgängliga böcker\n"
                    "5. Visa utlånade böcker\n"
                    "6. Logga ut\n")
                choice = input("Ange ditt val: ")

                if choice == "1":
                    bookTitle = input("Ange titel på boken du vill lägga till: ")
                    bookAuthor = input("Ange författare på boken du vill lägga till: ")
                    result = library.addBook(bookTitle, bookAuthor)
                    print(result)

                elif choice == "2":
                    bookTitle = input("Ange titel på boken du vill ta bort: ")
                    result = library.removeBook(bookTitle)
                    print(result)

                elif choice == "3":
                    result = library.displayAllBooks()
                    print(result)

                elif choice == "4":
                    result= library.displayAvailableBooks()
                    print(result)

                elif choice == "5":
                    result= library.displayBorrowedBooks()
                    print(result)

                elif choice == "6":
                    print("Du är nu utloggad som bibliotekarie.")
                    break

                else:
                    print("Ogiltigt val. Försök igen.")

        elif choice == "2":
            print("Du är nu inloggad som låntagare.")
            while True:
                print("\nVad vill du göra?:\n"
                    "1. Se tillgängliga böcker\n"
                    "2. Låna en bok\n"
                    "3. Lämna tillbaka en bok\n"
                    "4. Logga ut\n")
                choice = input("Ange ditt val: ")

                if choice == "1":
                    result = library.displayAvailableBooks()
                    print(result)

                elif choice == "2":
                    bookTitle = input("Ange titel på boken du vill låna: ")
                    result = library.borrowBook(bookTitle)
                    print(result)

                elif choice == "3":
                    bookTitle = input("Ange titel på boken du vill lämna tillbaka: ")
                    result = library.returnBook(bookTitle)
                    print(result)

                elif choice == "4":
                    print("Du är nu utloggad som låntagare.")
                    break

                else:
                    print("Ogiltigt val. Försök igen.")

        elif choice == "3":
            print("Du har valt att avsluta programmet.")
            is_running = False

        else: 
            print("Ogiltigt val. Försök igen.")
    except ValueError:
        print("Felaktig inmatning. Vänligen ange en siffra.")

