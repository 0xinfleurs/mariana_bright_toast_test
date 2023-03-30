import streamlit as st

st.set_page_config(layout='wide')
st.image('./header.png')
st.title("prediction for lol")
st.text("predicts the winner based on team and champions")

team_name = st.text_imput('What s )