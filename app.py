import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Student Performance Analysis")

st.write("Upload a CSV file to analyze student performance.")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    st.subheader("Preview of Data")
    st.dataframe(df.head())

    st.subheader("Summary Statistics")
    st.write(df.describe())

    st.subheader("Correlation Heatmap")
    st.write("Shows how different variables are related to performance.")

    fig, ax = plt.subplots(figsize=(10, 6))
    cax = ax.matshow(df.corr(), cmap="coolwarm")
    fig.colorbar(cax)
    st.pyplot(fig)

    st.subheader("Column-wise Analysis")
    column = st.selectbox("Select a column to analyze", df.columns)

    fig2, ax2 = plt.subplots()
    ax2.hist(df[column].dropna(), bins=20)
    ax2.set_title(f"Distribution of {column}")
    st.pyplot(fig2)

st.info("Made by Stanzin • Student Performance Dashboard")

