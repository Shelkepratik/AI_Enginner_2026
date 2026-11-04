from fastapi import FastAPI

app=FastAPI()

@app.get("/train")
def list_of_train():
    return{
        "train1":"name1",
        "train2":"name2",
        "train3":"name3",
        "train4":"name4",

    }