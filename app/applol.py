import streamlit as st

st.set_page_config(layout='wide')
#st.image('./header.png')
st.title("ML model for Esports betting")
st.text("This amazing machine learning model predicts the probability to win a game based upon each element of the team and the champions they're using")

team_name = st.text_imput('Tell us about your team')
champions = st.multiselect('Select a champion',[ 'champ1', 'champ2', 'champ3'])