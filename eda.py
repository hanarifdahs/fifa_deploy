import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   
import plotly.express as px
from PIL import Image

def run():
    st.title("FIFA 2022 Player Rating Prediction")

    #Tambahkan gambar
    img = Image.open("bola.jpeg")
    st.image(img, caption='Bola')

    #Load data
    data = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.3/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    st.dataframe(data)

    #Membuat barplot
    st.write("### Plot Attacking Work Rate")
    fig = plt.figure(figsize=(10, 5))
    sns.countplot(x = 'AttackingWorkRate', data = data)
    st.pyplot(fig)

    #Membuat Histogram dengan opsi dinamis
    st.write("### Histogram dengan opsi user input")
    options = st.selectbox("Pilih kolom untuk hisogram", ('Age', 'Overall'))
    fig = plt.figure(figsize=(10, 5))
    sns.histplot(data[options], bins=30, kde=True)
    st.pyplot(fig)

    #plotly
    st.write("### Price vs Rating")
    fig = px.scatter(data, x='ValueEUR', y = 'Overall', hover_data=['Name', 'Age'])
    st.plotly_chart(fig)


if __name__ == "__main__":
    run()