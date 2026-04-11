import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("🚗 Dashboard Smart City : Prédiction du Trafic")

st.write("Ce dashboard explique les prédictions de notre modèle d'IA.")

# (Ici, en situation réelle, on chargerait le modèle sauvegardé)

st.subheader("Importance des variables (Feature Importance)")
st.write("Qu'est-ce qui influence le plus le trafic ?")

# Recréer l'importance (à adapter avec ton vrai modèle)
# importances = model.feature_importances_
features = ['heure', 'jour_semaine', 'mois', 'est_weekend', 'temperature', 'pluie', 'trafic_moyen_3h']
importances = [0.4, 0.1, 0.05, 0.15, 0.1, 0.05, 0.15] # Valeurs fictives pour l'exemple

fig, ax = plt.subplots()
ax.barh(features, importances, color='skyblue')
st.pyplot(fig)

st.write("On remarque que **l'heure de la journée** est le facteur le plus critique pour prédire le trafic.")