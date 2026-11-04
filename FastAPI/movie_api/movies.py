from fastapi import FastAPI
app=FastAPI()

@app.get("/movies")
def list_of_movies():
    return{
              "movie1":{
                  "movie_name":"chhaava",
                  "language":"Marathi",
                  "genre":"Historical",
                  "duration_min":155,
                  "show_time":"06:30 PM",
                  "screen_number":1,
                  "ticket_price":200,
                  "seats_left":45
              },

              "movie2":
              {
                  "movie_name":"Dangal",
                  "language":"Hindi",
                  "genre":"sport Drama",
                  "duration_mins":161,
                  "show_time":"03:00 PM",
                  "screen_number":2,
                  "ticket_price":180,
                  "sets_left":30
                
              },

             "movie3": {
            "movie_name": "Inception",
            "language": "English",
            "genre": "Sci-Fi",
            "duration_mins": 148,
            "show_time": "09:00 PM",
            "screen_number": 3,
            "ticket_price": 250,
            "seats_left": 20
        },

        "movie4": {
            "movie_name": "Sairat",
            "language": "Marathi",
            "genre": "Romance",
            "duration_mins": 174,
            "show_time": "12:00 PM",
            "screen_number": 4,
            "ticket_price": 150,
            "seats_left": 50
        }
    }


    