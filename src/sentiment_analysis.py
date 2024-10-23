import spacy
from textblob import TextBlob

nlp = spacy.load("en_core_web_sm")

def classify_sentiment(sentiment_score):
    """Classifica o sentimento com base no score."""
    if sentiment_score > 0.1:
        return "Positivo"
    elif sentiment_score < -0.1:
        return "Negativo"
    else:
        return "Neutro"

def analyze_sentiment(text):
    """Realiza a análise de sentimentos no texto fornecido."""
    doc = nlp(text)
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    sentiment_classification = classify_sentiment(sentiment_score)
    return sentiment_classification, sentiment_score
