import streamlit as st
from streamlit import session_state as ss
from pages.modules.display_poster import display_poster
def main():
    tab1, tab2 = st.tabs(["Games you liked","Games you disliked"])
    def show_games(id_set):
        col1, col2,col3= st.columns(3,gap="large")
        i=0
        for id in id_set:
            if i%3==0:
                display_poster(id,col1,callback_func=None,display_like=False)
            elif i%3==1:
                display_poster(id,col2,callback_func=None,display_like=False)
            else:
                display_poster(id,col3,callback_func=None,display_like=False)
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
        