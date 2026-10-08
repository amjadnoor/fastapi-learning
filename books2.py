from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    description: str
    rating: float

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: float

BOOKS = [
    Book(1, "The Midnight Library", "Matt Haig", "Between life and death there is a library containing an infinite number of books, each one the story of another reality you could have lived if you had made a different choice", 4.3),
    Book(2, "Where the Crawdads Sing", "Delia Owens", "A touching coming-of-age story and a surprising murder mystery centered around Kya Clark, the 'Marsh Girl' who grew up isolated in the North Carolina wild", 4.5),
    Book(3, "Project Hail Mary", "Andy Weir", "A lone astronaut must use his scientific ingenuity to solve a space-faring mystery and save Earth from an extinction-level event", 4.7),
    Book(4, "Educated", "Tara Westover", "An unforgettable memoir about a young girl who escapes her survivalist family in rural Idaho to pursue a university education, stepping into the classroom for the very first time at age seventeen", 4.6),
    Book(5, "Atomic Habits", "James Clear", "A practical guide that breaks down complex behaviors into simple, daily habits to help you transform your life and achieve remarkable results", 4.8),
    Book(6, "The Silent Patient", "Alex Michaelides", "A shocking psychological thriller about a famous painter who shoots her husband and then refuses to speak another word, and the criminal psychotherapist determined to uncover her motive", 4.2)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(new_book)