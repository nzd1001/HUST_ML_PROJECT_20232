from streamlit_option_menu import option_menu
from pages.profile import main as profile_main
from pages.search import main as search_main
selected=option_menu(
    menu_title=None,
    options=["Profile","Search","Recommendation"],
    icons=["person","search","controller"],
    orientation="horizontal"
)
if selected=="Search":
    search_main()
elif selected=="Profile":
    profile_main()
elif selected=="Recommendation":
    pass
