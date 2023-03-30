import streamlit as st
import numpy as np
import pandas as pd
import requests

st.set_page_config(layout='wide')
st.title(":sparkler: Welcome to Bright Toasts! :sparkler:")
st.text("Bright Toasts is a powerful machine learning model that given a description of your ideal wine gives you the perfect matches for your next wine tasting! ")
#st.image('./header.png')


element = st.empty()
element = st.empty()
clicked = st.button ("Click to find your Bright Toast...:sparkles:")




if clicked:
    st.markdown(":star2: These are optional parameters, don't worry if you don't know :) ")
    st.selectbox('Select', ['white','red'])
    country = st.multiselect('select a country', ['Italy', 'Portugal', 'US', 'Spain', 'France', 'Germany',
       'Argentina', 'Chile', 'Australia', 'Austria', 'South Africa',
       'New Zealand', 'Israel', 'Hungary', 'Greece', 'Romania', 'Mexico',
       'Canada', 'Turkey', 'Czech Republic', 'Slovenia', 'Croatia',
       'Georgia', 'Uruguay', 'England', 'Lebanon', 'Serbia', 'Brazil',
       'Moldova', 'Morocco', 'Peru', 'India', 'Bulgaria', 'Cyprus',
       'Armenia', 'Switzerland', 'Bosnia and Herzegovina', 'Slovakia',
       'Macedonia', 'Ukraine', 'Luxembourg', 'China', 'Egypt'])
    st.markdown(":star2: However, the description is mandatory! ")
    description  = st.text_input('Describe your ideal wine making sure to detail the look, smell, and taste.')
    st.markdown(":star2: Example of a correct wine description: Aromas include tropical fruit, broom, brimstone and dried herb. The palate isn't overly expressive, offering unripened apple, citrus and dried sage alongside brisk acidity.")








## Let's call our API in order to retreive a prediction

#url = 'x'
   # if url == 'x'

#params ={'colour'; colour,
         #'country'; country
         # 'description';description,}

#req = requests.get(url, params=params)
# req.json()
