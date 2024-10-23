from .sentiment_analysis import analyze_sentiment
from .entity_extraction import extract_entities
from .summarization import summarize_text

def analyze_feedback(feedback_text):
    """Função que analisa o feedback recebido."""
    sentiment_classification, sentiment_score = analyze_sentiment(feedback_text)
    entities = extract_entities(feedback_text)
    summary = summarize_text(feedback_text)
    
    return {
        'sentiment_classification': sentiment_classification,
        'sentiment_score': sentiment_score,
        'entities': entities,
        'summary': summary
    }

if __name__ == "__main__":
    test_feedback = "Adorei o novo modelo de celular da MarcaX, tem ótimo desempenho! O serviço de entrega da loja Y foi péssimo."
    results = analyze_feedback(test_feedback)
    print(f"Sentimento: {results['sentiment_classification']}")
    print(f"Score: {results['sentiment_score']}")
    print(f"Entidades: {results['entities']}")
    print(f"Resumo: {results['summary']}")
