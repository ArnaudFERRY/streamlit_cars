# Etape 2 : requirements.txt
# Ce fichier doit comporter les versions des modules à importer, au format ci-dessous. Evidemment les numéros de versions doivent être adaptés à ce qui est utilisé par ton code, ne recopie donc pas les valeurs ci-dessous, qui sont uniquement là pour te montrer le format attendu dans ce fichier.

# numpy==1.19.2
# seaborn==0.11.0
# pandas==1.1.3
# streamlit==0.79.0



import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

### Chargement des données
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

# Nettoyage : Suppression des espaces
df_cars['continent'] = df_cars['continent'].apply(lambda x: str(x).strip())



# Créer deux colonnes pour afficher le contenu

col1, col2 = st.columns(2)


# Affichage du contenu dans la première colonne
with col1:
    # st.header("Colonne 1")
    # st.write("Ceci est du texte dans la première colonne.")
    # st.write("Vous pouvez ajouter d'autres éléments ici, comme des images, des graphiques, etc.")
    
    st.header("Heatmap correlation Dataset cars")
    df_corr = df_cars.select_dtypes(include = ['number'])
    palette = sns.diverging_palette(250, 30, l=65, center="dark", as_cmap=True)
    heatmap_correlation = sns.heatmap(df_corr.corr(), cmap=palette, center=0)
    st.pyplot(heatmap_correlation.figure)
    
    st.subheader("Analyse de la Heatmap correlation")
    st.write("Il y'a une très forte corrélation entre hp (horsepower) et ces variables : cylinders, cubicinches, weightlbs")

# Affichage du contenu dans la deuxième colonne
with col2:
    # st.header("Colonne 2")
    # st.write("Ceci est du texte dans la deuxième colonne.")
    # st.write("Vous pouvez également personnaliser le contenu de cette colonne avec différentes informations.")
    st.header("Production by region")
        
    # Construction des DataFrames par région
    df_dict = {
        'all': pd.DataFrame(df_cars),
        'us': pd.DataFrame(df_cars.loc[df_cars['continent'] == 'US.']),
        'europe': pd.DataFrame(df_cars.loc[df_cars['continent'] == 'Europe.']),
        'japan': pd.DataFrame(df_cars.loc[df_cars['continent'] == 'Japan.'])
    }
    
    # Choix de la région
    region = st.selectbox('Region', ('us', 'europe', 'japan'))
    
    # Sélection du DataFrame en fonction de la région
    if region in df_dict:
        df_region = df_dict[region]
    else:
        st.write("Choix invalide")
    
    # Créer deux sous-colonnes pour les graphiques
    col3, col4 = st.columns(2)
    
    # Affichage de l'histogramme
    with col3:
        st.header(f"hp by year for {region}")
        st.bar_chart(data=df_region, x='year', y='hp', use_container_width=True)
    
    # Affichage du scatterplot
    with col4:
        st.header(f"mpg by horsepower for {region}")
        fig, ax = plt.subplots()
        ax.scatter(df_region['hp'], df_region['mpg'])
        ax.set_xlabel('hp')
        ax.set_ylabel('mpg')
        st.pyplot(fig)
    
