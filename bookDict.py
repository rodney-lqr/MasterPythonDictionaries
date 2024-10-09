# Creating a Dictionary of books

#Book One
book1 = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "genre": "Fiction",
    "year": 1960
}

#Book Two
book2 = {
    "title": "1984",
    "author": "George Orwell",
    "genre": "Dystopian",
    "year": 1949  
}

#Book Three
book3 = {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "genre": "Classic",
    "year": 1925
}

#Book Four
book4 = {"title": "Moby Dick",
    "author": "Herman Melville",
    "genre": "Adventure",
    "year": 1851
    }

#Book Five
book5 = {"title": "Pride and Prejudice",
    "author": "Jane Austen",
    "genre": "Romance",
    "year": 1813
    }

allBooks = (book1, book2, book3, book4, book5)

for i, book in enumerate(allBooks):
    print(f"Book {i+1}: {book}")
