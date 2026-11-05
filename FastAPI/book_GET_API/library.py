from fastapi import FastAPI,Path
import json

app=FastAPI()


def show_book():
    with open("books.json","r") as book:
        book=json.load(book)
        return book

@app.get("/")
def greet():
    return {"message":"welcome to the city Library API"}

#GET API-Library information
@app.get("/about")
def about():
    return{
        "name":"city library",
        "city":"pune",
        "opening_hourse":"9:00 AM to 8:00 PM"
    }


@app.get("/books")
def load_books():
    book=show_book()
    return book

@app.get("/books/{book_id}")
def book_id(book_id:str=Path(...,description="ID of book",example="B001")):
    book=show_book()
    for book_id in book:
        return book[book_id]
    return {"error":"Book not found"}
   

