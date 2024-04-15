import streamlit as st
from streamlit import session_state as ss
import pickle 
import pandas as pd
from pages.modules.display_poster import display_poster
import streamlit as st
def main():
    games=pd.DataFrame(ss.game_data)
    games=games[:10000]
    
    chosen_game=st.selectbox("Select the game you interested in",games["title"])
    @st.cache_data
    def tag_sim_load():
        with open("pkl_files/10000_tag_sim.pkl","rb") as tag_sim_pkl:
            return pickle.load(tag_sim_pkl)
    tag_sim=tag_sim_load()
    def recommend(game,sim):
        index=games[games["title"]==game].index[0]
        top_rec=sorted(list(enumerate(sim[index])),key=lambda x:x[1],reverse=True)
        return top_rec[0:15]
    if "rec_clicked" not in ss:
        ss.rec_clicked=False
    def show_recommend():
        col1, col2,col3 = st.columns(3,gap="large")
        i=0
        for candidate in recommend(chosen_game,tag_sim):
            if i%3==0:
                display_poster(games.iloc[candidate[0]]["app_id"],col1)
            elif i%3==1:
                display_poster(games.iloc[candidate[0]]["app_id"],col2)
            else:
                display_poster(games.iloc[candidate[0]]["app_id"],col3)
            i+=1
    def rec_callback():
        ss.rec_clicked=True
    if st.button("Search"):
        ss.rec_clicked = True
    if ss.rec_clicked:
        show_recommend()
if __name__=="__main__":
    main()