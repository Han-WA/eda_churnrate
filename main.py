import streamlit as st
from streamlit_option_menu import option_menu

import about, uni, bi, multi, conc

st.set_page_config(page_title = "EDA")

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
                "title" : title,
                "function" : function
            })
        
    def run():
        app = option_menu(
            menu_title = 'EDA on Telecom Company Customer Churn Rate',
            options = ['Data','Univariate', 'Bivariate','Multivariate', 'Conclusion'],
            icons = ["database-fill-gear","clipboard2-check-fill","clipboard2-data-fill", "clipboard2-heart-fill"],
            menu_icon = "graph-down", 
            default_index = 0,
            orientation = "horizontal", 
        )
        if app == "Data":
            about.app()
        if app == "Univariate":
            uni.app()
        if app == "Bivariate":
            bi.app()
        if app == "Multivariate":
            multi.app()
        if app == "Conclusion":
            conc.app()

    run()