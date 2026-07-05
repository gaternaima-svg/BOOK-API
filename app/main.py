from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return {"message":"Bienvenue sur Book API"}
@app.get("/books")
def books():
    return{
        "books":[
            {"id":1,"title":"python"},
            {"id":2,"title":"FastAPI"}
        ]
    }
@app.get("/authors")
def authors():
    return {
        "authors": [
            {"id": 1,"name":"Guido van Rossum"},
            {"id":2,"name":"Sebastien Ramirez"}
        ]
    }