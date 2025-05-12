from langdetect import detect
from textblob import TextBlob

def check_language(text: str):
    return f"La lingua rilevata è: {detect(text)}. "


def check_sentiment(text: str):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
        
    # Se sentiment > 0 allora -> positivo
    # Se sentiment < 0 allora -> negativo
    # Se sentiment = 0 allora -> neutro

    if sentiment > 0:
        return "Il sentiment è positivo"
    elif sentiment < 0:
        return "Il sentiment è negativo"
    else:
        return "Il sentiment è neutrale"
