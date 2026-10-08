from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: float
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="Id is not needed on create", default=None)
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=200)
    rating: float = Field(ge=0, le=5)
    published_date: int = Field(gt=1999, lt=2031)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "Amjad",
                "description": "A new description of a book",
                "rating": 5,
                "published_date": 2012
            }
        }
    }

BOOKS = [
    Book(1, "The Midnight Library", "Matt Haig", "Between life and death there is a library containing an infinite number of books, each one the story of another reality you could have lived if you had made a different choice", 4.3, 2003),
    Book(2, "Where the Crawdads Sing", "Delia Owens", "A touching coming-of-age story and a surprising murder mystery centered around Kya Clark, the 'Marsh Girl' who grew up isolated in the North Carolina wild", 4.5, 2025),
    Book(3, "Project Hail Mary", "Andy Weir", "A lone astronaut must use his scientific ingenuity to solve a space-faring mystery and save Earth from an extinction-level event", 4.7, 2004),
    Book(4, "Educated", "Tara Westover", "An unforgettable memoir about a young girl who escapes her survivalist family in rural Idaho to pursue a university education, stepping into the classroom for the very first time at age seventeen", 4.6, 2000),
    Book(5, "Atomic Habits", "James Clear", "A practical guide that breaks down complex behaviors into simple, daily habits to help you transform your life and achieve remarkable results", 4.8, 2019),
    Book(6, "The Silent Patient", "Alex Michaelides", "A shocking psychological thriller about a famous painter who shoots her husband and then refuses to speak another word, and the criminal psychotherapist determined to uncover her motive", 4.2, 2013)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_id}")
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.get("/books/")
async def read_books_by_rating(book_rating: float):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)

    return books_to_return

@app.get("/book/publish/")
async def read_books_by_publish_date(published_date: int):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)

    return books_to_return

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    if len(BOOKS) > 0:
        book.id = BOOKS[-1].id + 1
    else:
        book.id = 1

    return book

@app.put("/books/update_book")
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break