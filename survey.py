import streamlit as st
from streamlit import session_state as ss
import pickle 
import pandas as pd
from pages.modules.display_poster import display_poster
st.set_page_config(layout="wide")
@st.cache_data
def load_game_data():
    with open("pkl_files/game.pkl","rb") as game_pkl:
        data=pickle.load(game_pkl)
    return data
ss.game_data=load_game_data()
games_id = [1638340,1446780,698780,264710]
col1, col2,col3 = st.columns(3,gap="large")
i=0
ss.rated={id:None for id in ss.game_data["app_id"]}
ss.liked=set()
ss.disliked=set()
for id in games_id:
    if i%3==0:
        display_poster(id,col1)
    elif i%3==1:
       display_poster(id,col2)
    else:
        display_poster(id,col3)
    i+=1
st.markdown("##")
submit_button=st.page_link("pages/main.py",label="SUBMIT")
