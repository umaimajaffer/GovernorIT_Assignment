import json
import os

LIBRARY_FILE = "library.json"

def load_library():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as f:
            return json.load(f)
    return []

def save_library(library):
    with open(LIBRARY_FILE, "w") as f:
        json.dump(library, f, indent=4)

def display_menu():
    print("\n📚 Personal Library Manager")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

def add_book(library):
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    try:
        year = int(input("Publication Year: "))
    except ValueError:
        print("❌ Invalid year.")
        return
    genre = input("Genre: ").strip()
    read = input("Have you read it? (y/n): ").lower() == "y"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }
    library.append(book)
    print("✅ Book added.")

def remove_book(library):
    title = input("Enter the title to remove: ").strip().lower()
    removed = False
    for book in library[:]:
        if book["title"].lower() == title:
            library.remove(book)
            removed = True
    if removed:
        print("✅ Book removed.")
    else:
        print("❌ Book not found.")

def search_books(library):
    keyword = input("Enter title or author to search: ").strip().lower()
    matches = [book for book in library if keyword in book["title"].lower() or keyword in book["author"].lower()]
    if matches:
        print(f"🔍 Found {len(matches)} matching book(s):")
        for book in matches:
            display_book(book)
    else:
        print("❌ No matches found.")

def display_all_books(library):
    if not library:
        print("📭 No books in library.")
    else:
        print(f"📖 Listing {len(library)} book(s):")
        for book in library:
            display_book(book)

def display_book(book):
    status = "✅ Read" if book["read"] else "📌 Unread"
    print(f"• {book['title']} by {book['author']} ({book['year']}), Genre: {book['genre']} - {status}")

def display_statistics(library):
    total = len(library)
    read_count = sum(1 for book in library if book["read"])
    if total == 0:
        print("📊 No books to calculate stats.")
        return
    percentage = (read_count / total) * 100
    print(f"📚 Total books: {total}")
    print(f"✅ Books read: {read_count} ({percentage:.2f}%)")

def main():
    library = load_library()

    while True:
        display_menu()
        choice = input("Select an option (1-6): ").strip()
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_books(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("👋 Goodbye! Library saved.")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == "__main__":
    main()
