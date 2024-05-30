from fastapi import FastAPI, Path, Query
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self, id, title, author, description, rating, published_date) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
        self.published_date = published_date


class BookRequest(BaseModel):
    id: Optional[int] = Field(title='id is not needed', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)
    published_date: int = Field(gt=1999, lt=2031)

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'Harry Pollo and the prisoner of gulag',
                'author': 'Manguito Lovebird',
                'description': 'an epic tale',
                'rating': 5,
                'published_date': 2018
            }
        }


BOOKS = [
    Book(1, 'Python for babies', 'python basics',
         'too difficult for 1 years old', 2, 2022),
    Book(2, 'How to train your lovebird',
         'Lovebird Owner', 'very informative', 4, 2018),
    Book(3, 'Harry pollo and the mystery of disappearing poo',
         'Manguito Lovebird', 'An epic story of this century', 5, 2021),
    Book(4, 'Harry Pollo and the chamber of millet',
         'Manguito Lovebird', 'great book', 5, 2022),
    Book(5, 'Harry Pollo and the order of grackles',
         'Manguito Lovebird', 'A very nice book', 5, 2023),
    Book(6, 'NodeJS for babies', 'javscript basics', 'It was okay', 3, 2023)
]


@app.get('/books')
async def get_all_books():
    return BOOKS


@app.get('/books/{book_id}')
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book


@app.get('/books/')
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []
    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)
    return books_to_return


@app.get('/books/publish/')
async def read_books_by_publish_date(published_date: int = Query(gt=1999, lt=2031)):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return


@app.post('/create-book')
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book


@app.put('/books/update_book')
async def update_book(book: BookRequest):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book


@app.delete('/books/{book_id}')
async def delete_book(book_id: int = Path(gt=0)):
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            break
