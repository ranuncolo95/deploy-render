from fastapi import FastAPI 
from langdetect import detect

app = FastAPI()
@app.get("/")
def homepage():
    return "Hello World"

users = []


@app.get("/nome")
def hello(nome: str, cognome: str):
    return f"Ciao, {nome} {cognome}"


@app.post("/aggiungi-utente")
def add_user(username: str):
    users.append(username)
    return f"Utente {username} aggiunto con successo."


@app.get("/cerca-utente")
def search_user(username: str):
    if username in users:
        return f"L'utente {username} esiste."
    else:
        return f"L'utente {username} non esiste."
    

@app.get("/totale-utenti")
def total_user():
    return f"Ci sono {len(users)} utenti registrati."


@app.delete("/elimina-utente")
def delete_user(username : str):
    if username in users:   
        users.remove(username)
        return f"Utente {username} eliminato con successo."
    else:
        return f"{username} non trovato."
    

#NEW API EX1

@app.get("/es1")
def check_language(text: str):
    return f"La lingua rilevata è: {detect(text)}"
