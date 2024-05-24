from fastapi import FastAPI, Body

app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int

    def __init__(self, id, title, author, description, rating) -> None:
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


BOOKS = [
    Book(1, 'Python for babies', 'python basics',
         'too difficult for 1 years old', 2),
    Book(2, 'How to train your lovebird',
         'Lovebird Owner', 'very informative', 4),
    Book(3, 'Harry pollo and the mystery of disappearing poo',
         'Manguito Lovebird', 'An epic story of this century', 5),
    Book(4, 'Harry Pollo and the chamber of millet',
         'Manguito Lovebird', 'great book', 5),
    Book(5, 'Harry Pollo and the order of grackles',
         'Manguito Lovebird', 'A very nice book', 5),
    Book(6, 'NodeJS for babies', 'javscript basics', 'It was okay', 3)
]


@app.get('/books')
async def get_all_books():
    return BOOKS


@app.post('/create-book')
async def create_book(book_request=Body()):
    BOOKS.append(book_request)
