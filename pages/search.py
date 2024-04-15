import streamlit as st
from streamlit import session_state as ss
import pickle 
import pandas as pd
import streamlit as st
def main():
    def display_poster(id,col,callback_func=None):
        row_index = ss.game_data[ss.game_data['app_id'] ==id].index[0]
        title = ss.game_data.iloc[row_index]['title']
        url=f"https://cdn.akamai.steamstatic.com/steam/apps/{id}/header.jpg?"
        col.write(title)
        col.image(url, width=350)
        rated=  col.radio(
        "",
        [ "Like","Dislike"],key=title+"radio",index=ss.rated[id],horizontal=True,on_change=callback_func
        )
        # Update like/dislike counts based on checkbox clicks
        if rated=="Like":
            ss.liked.add(id)
            ss.rated[id]=0
        elif rated=="Dislike":
            ss.disliked.add(id)
            ss.rated[id]=1
    games=pd.DataFrame(ss.game_data)
    games=games[:10000]
    st.title("Games Recommender")
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
        col1, col2 = st.columns(2,gap="large")
        i=0
        for candidate in recommend(chosen_game,tag_sim):
            if i%2==0:
                display_poster(games.iloc[candidate[0]].app_id,col1,callback_func=rec_callback)
            else:
                display_poster(games.iloc[candidate[0]].app_id,col2,callback_func=rec_callback)
            i+=1
    def rec_callback():
        ss.rec_clicked=True
    if st.button("Search"):
        ss.rec_clicked = True
    if ss.rec_clicked:
        show_recommend()
if __name__=="__main__":
    main()