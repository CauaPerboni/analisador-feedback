# app.py

import streamlit as st
from src.analyzer import analyze_feedback

st.title("Analisador de Feedback")

feedback_text = st.text_area("Deixe seu feedback:", height=200)

if st.button("Analisar"):
    if feedback_text:
        results = analyze_feedback(feedback_text)
        st.subheader("Resultados da Análise")
        
        st.write(f"**Classificação do Sentimento:** {results['sentiment_classification']}")
        st.write(f"**Score de Sentimento:** {results['sentiment_score']}")
        
        st.write("**Entidades Encontradas:**")
        for entity, label in results['entities']:
            st.write(f"- {entity} (Tipo: {label})")
        
        st.write("**Resumo:**")
        st.write(results['summary'])
    else:
        st.warning("Por favor, insira algum feedback antes de analisar.")
