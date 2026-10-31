
class LibraryManager:
    def __init__(self):
        self.books = []

        while True:
            print("""
            1. Add a Book
            2. Remove a Book
            3. Show All Books
            4. Exit
            """)

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_book()

            elif choice == "2":
                self.remove_book()

            elif choice == "3":
                self.show_books()

            elif choice == "4":
                print("Thank you for using Library Manager!")
                break

            else:
                print("Invalid choice!")

    def add_book(self):
        book_name = input("Enter book name: ")
        self.books.append(book_name)
        print("Book added successfully!")

    def remove_book(self):
        book_name = input("Enter book name to remove: ")

        if book_name in self.books:
            self.books.remove(book_name)
            print("Book removed successfully!")
        else:
            print("Book not found")

    def show_books(self):
        if len(self.books) > 0:
            print("Available books:")
            for book in self.books:
                print(book)
        else:
            print("No books available in the library!")


library = LibraryManager()
