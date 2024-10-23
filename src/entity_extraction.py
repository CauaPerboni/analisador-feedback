import spacy

nlp = spacy.load('en_core_web_sm')

def extract_entities(text):
    """
    Função para extrair entidades nomeadas (NER) de um texto.
    Retorna uma lista de entidades encontradas no formato (entidade, tipo).
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return entities

if __name__ == "__main__":
    test_text = "Adorei o novo modelo de celular da MarcaX, tem ótimo desempenho!"
    print(f"Entidades encontradas: {extract_entities(test_text)}")
