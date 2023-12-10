## **Introduktion**

- Ert lokala bibliotek har kommit till er för hjälp att skapa ett system för att hålla reda på vilka böcker de har, och hantera vilka böcker som är utlånade/finns att låna.

## **Specifikation**

**LibrarySystem (Godkänt)**

- Skapa en class vid namn LibrarySystem, denna class skall ha två attribut “name” som är namnet på biblioteket, samt “books” som är en lista av alla böcker som biblioteket har. CHECK!

- Classen skall ha metoder för att kunna göra följande:
    - Lägga till en bok CHECK
    - Ta bort en bok CHECK
    - Markera en bok som utlånad CHECK
    - Markera en bok som återlämnad CHECK
    - Se om en bok är tillgänglig CHECK
    - Skriva ut alla titlar som finns tillgängliga (som alltså inte är utlånade) CHECK

- När man kallar på respektive metod, skall den också printa ut vad som skett. Om man t.ex. kallar på metoden som skall markera en bok som utlånad skall den dels markera boken som utlånad, men också printa ut ett meddelande (Bok X har markerats som utlånad).

- “books” är som tidigare nämnt en lista av böcker som classen har som attribut, denna lista skall då innehålla en datastruktur som representerar varje enskild bok. Varje bok skall innehålla information om bokens titel, författare samt om den är utlånad eller inte. Fundera på vilken datatyp som passar bäst för detta.

- När du implementerat classen, skapa en instans av denna med 2 olika böcker, och kalla på samtliga av metoderna, en i taget, på instansen för att t.ex. lägga till böcker, markera bok som återlämnad, etc.

**LibrarySystem (Väl Godkänt)**

- Nedan är en beskrivning för hur du skall utveckla din **LibrarySystem** class för att hålla reda på återlämningsdatum.

**Denna uppgift behöver endast göras av de som har ambitionen att uppnå betyget Väl Godkänt.**

- Biblioteket vill hålla reda på med hur många dagar en bok är försenad när den lämnas tillbaka. Biblioteket erbjuder kunder att låna böcker under 14 dagar.

- När man kallar på metoden för att återlämna en bok, skall den som tidigare markeras som återlämnad och printa ut detta, men också, om boken är försenad, printa ut med hur många dagar den är försenad.

- Tips:
    - Du behöver hålla reda på datumet som boken lånades för respektive bok, utöver att hålla reda på om den blivit utlånad eller ej.
    - När en bok markeras som utlånad så kan du utgå från att detta sker på samma dag, så du kan använda datetime.datetime.now() för att hämta ut det aktuella datumet.
    - Du kan använda en hjälpmetod t.ex. calculate_overdue_days som du kallar på från metoden som markerar en bok som återlämnad, för att göra logiken mer uppdelad.

**TestLibrarySystem**

- Importera unittest till din fil och skapa en class vid namn **TestLibrarySystem** som ärver från unittest.TestCase, och som testar respektive metod från din **LibrarySystem** class.

## **Begränsningar**

- Anta att det bara finns ett exemplar av varje bok. I vanliga fall har sannolikt ett bibliotek t.ex. 10 exemplar av Harry Potter, men i detta fall, för att underlätta uppgiften, har biblioteket endast 1 exemplar av varje bok.

