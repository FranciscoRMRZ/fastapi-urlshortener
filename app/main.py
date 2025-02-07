from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Hello FastAPI"

@app.post("/shorten-url")
async def shortURL():
    return 'return-short-url-1234'

@app.get("/{url_id}")
async def redirectToURL(url_id):
    return f'redirect to {url_id} '
