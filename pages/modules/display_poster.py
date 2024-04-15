import streamlit as st
from streamlit import session_state as ss
from annotated_text import annotated_text
def display_poster(id,col,callback_func=None,display_like=True):
    row_index = ss.game_data[ss.game_data['app_id'] ==id].index[0]
    title = ss.game_data.iloc[row_index]['title']
    url=f"https://cdn.akamai.steamstatic.com/steam/apps/{id}/header.jpg?"
    col.write(title)
    col.image(url, width=350)
    with col.popover("Show info"):
        st.write("#Genres:")
        """tags=[]
        colors=["#63abbd"]
        i=0
        for tag in ss.game_data.iloc[row_index]["tags"][:5]:
            tags.append((tag,"",colors[i%len(colors)]))
            tags.append(" ")
            i+=1
        if len(tags)!=0:
            tags.pop()
            with col:
                annotated_text(tags)"""
        tags=[tag for tag in ss.game_data.iloc[row_index]["tags"]]
        st.markdown(" | ".join(tags))
        st.markdown("#Description:\t "+ss.game_data.iloc[row_index]["description"])
    if display_like:
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