from spacy.lang.en import English
from collections import Counter

nlp = English()
nlp.add_pipe('sentencizer')

def summarize_text(text, num_sentences=2):
    """
    Função para sumarizar um texto selecionando as frases mais frequentes.
    O resumo é feito com base nas palavras mais comuns.
    """
    doc = nlp(text)
    sentences = [sent.text.strip() for sent in doc.sents]

    # Tokenizar e contar frequência de palavras
    word_frequencies = Counter([token.text.lower() for token in nlp(text) if not token.is_stop and not token.is_punct])
    
    # Classificar frases pela soma da frequência das palavras
    sentence_scores = {}
    for sent in sentences:
        sentence_scores[sent] = sum(word_frequencies.get(word.text.lower(), 0) for word in nlp(sent))
    
    # Selecionar as frases mais relevantes
    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    # Juntar as frases resumidas em um texto final
    summary = ' '.join(summarized_sentences)
    
    return summary

if __name__ == "__main__":
    test_text = "Adorei o novo modelo de celular da MarcaX, tem ótimo desempenho! O serviço de entrega da loja Y foi péssimo, demorou mais de uma semana. Produto com preço excelente, mas a qualidade deixou a desejar. Ótima experiência na compra, recomendo a loja Z para todos."
    print(f"Resumo: {summarize_text(test_text)}")
