from fastapi import FastAPI, Body

app = FastAPI()

BOOKS = [
  {
    "title": "The 3-Body Problem",
    "author": "Cixin Liu",
    "category": "Science Fiction"
  },
  {
    "title": "The Hobbit",
    "author": "J.R.R. Tolkien",
    "category": "Fantasy"
  },
  {
    "title": "Moby Dick",
    "author": "Herman Melville",
    "category": "Classic"
  },
  {
    "title": "Superintelligence",
    "author": "Nick Bostrom",
    "category": "Non-Fiction"
  },
  {
    "title": "Project Hail Mary",
    "author": "Andy Weir",
    "category": "Science Fiction"
  },
  {
    "title": "Thinking, Fast and Slow",
    "author": "Daniel Kahneman",
    "category": "Non-Fiction"
  }
]


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get('title').casefold() == book_title.casefold():
            return book

@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

    return books_to_return

@app.get("/books/{book_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    book_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and book.get('category').casefold() == category.casefold():
            book_to_return.append(book)

    return book_to_return

@app.post("/books/create_book")
async def create_book(new_book = Body()):
    BOOKS.append(new_book)

@app.put("/books/update_book")
async def update_book(updated_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == updated_book.get('title').casefold():
            BOOKS[i] = updated_book

@app.delete("/books/delete_book/{book_title}")
async def delete_book(book_title: str):
    for i in range(len(BOOKS)):
      if BOOKS[i].get('title').casefold() == book_title.casefold():
          BOOKS.pop(i)
          break