import pandas as pd
import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("Sankey Diagrams of Japanese Timber Flows", anchor=None)

st.markdown("**Author**: [Takuma Watari](https://takuma-watari.com/en/) (National Institute for Environmental Studies, Japan)")

st.markdown(
    """
    **Aim**: This web application presents Sankey diagrams of timber flows in Japan from 1960 to 2023.
    
    **Data sources**: All primary data used in this analysis comes from databases maintained by the Japanese government and industry organisations.
    
    **Software**: The Sankey diagrams are designed using [floWeaver software](https://github.com/ricklupton/floweaver).
    """
)

available_years = list(range(1960, 2024))
year = st.select_slider('Year', options=available_years)

with open("sankey/" + f'{year}.svg', encoding="utf8") as file:
    svg_content = file.read()
st.markdown(f'<div style="justify-content: center;">{svg_content}</div>', unsafe_allow_html=True)