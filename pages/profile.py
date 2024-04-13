import streamlit as st
from streamlit import session_state as ss
def main():
    tab1, tab2 = st.tabs(["Games you liked","Games you disliked"])
    def display_poster(id,col,callback_func=None):
        row_index = ss.game_data[ss.game_data['app_id'] ==id].index[0]
        title = ss.game_data.iloc[row_index]['title']
        url=f"https://cdn.akamai.steamstatic.com/steam/apps/{id}/header.jpg?"
        col.write(title)
        col.image(url, width=350)   
    def show_games(id_set):
        col1, col2= st.columns(2,gap="large")
        i=0
        for candidate_id in id_set:
            if i%3==0:
                display_poster(candidate_id,col1)
            else:
                display_poster(candidate_id,col2)
            i+=1
    with tab1:
        show_games(ss.liked)
    with tab2:
        show_games(ss.disliked)
    font_css = """
    <style>
    button[data-baseweb="tab"] > div[data-testid="stMarkdownContainer"] > p {
    font-size: 18px;
    }
    </style>
    """
    st.write(font_css, unsafe_allow_html=True)
if __name__=="__main__":
    main()
        