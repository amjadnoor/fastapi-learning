from fastapi import FastAPI

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