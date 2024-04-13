import streamlit as st
from streamlit import session_state as ss
import pickle 
import pandas as pd
@st.cache_data
def load_game_data():
    with open("pkl_files/game.pkl","rb") as game_pkl:
        data=pickle.load(game_pkl)
    return data
ss.game_data=load_game_data()
def display_poster(id,col):
    row_index = ss.game_data[ss.game_data['app_id'] ==id].index[0]
    title = ss.game_data.iloc[row_index]['title']
    url=f"https://cdn.akamai.steamstatic.com/steam/apps/{id}/header.jpg?"
    col.write(title)
    col.image(url, width=350)
    rated=  col.radio(
    "",
    [  "Like","Dislike"],key=title+"radio",index=ss.rated[id],horizontal=True
    )
    # Update like/dislike counts based on checkbox clicks
    if rated=="Like":
        ss.liked.add(id)
        ss.rated[id]=0
    elif rated=="Dislike":
        ss.disliked.add(id)
        ss.rated[id]=1
games_id = [1638340,1446780,698780,264710]
col1, col2 = st.columns(2,gap="large")
i=0
ss.rated={id:None for id in ss.game_data["app_id"]}
ss.liked=set()
ss.disliked=set()
for id in games_id:
    if i%2==0:
        display_poster(id,col1)
    else:
       display_poster(id,col2)
    i+=1
st.markdown("##")
submit_button=st.page_link("pages/main.py",label="SUBMIT")
