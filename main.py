from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from defs import *

app = FastAPI()
users = []
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def homepage(request: Request, response_class=HTMLResponse):
    return templates.TemplateResponse("index.html", {"request": request})


class TextInput(BaseModel):
    text: str


@app.post("/process")
async def process_text(input_data: TextInput):
    user_input = input_data.text
    result_lang = check_language(user_input)
    result_sent = check_sentiment(user_input)

    return {"result" : result_lang + result_sent}


