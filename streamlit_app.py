import streamlit as st
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
import base64
import time
from datetime import datetime

# Set up the page
st.set_page_config(page_title="Home", page_icon=":milky_way:")

# hide_default_format = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """
# st.markdown(hide_default_format, unsafe_allow_html=True)

st.header("About Me", divider='rainbow')
col1, col2 = st.columns(2)

with col1:
    
    st.markdown('<div style="text-align: justify;">Hello, I’m Praza, an Atmospheric and Planetary Sciences grad with a big interest in creating N-Body simulations, modeling the trajectories or orbits of small solar system bodies, analyzing their orbital evolution and dynamics, and studying exoplanet systems. This website contains my coursework as a student and a few other small astronomy-related topics.</div>', unsafe_allow_html=True)
    st.subheader("Get in touch on me ", divider='rainbow')
    st.markdown("""[LinkedIn](https://www.linkedin.com/in/praza-kembaren) | [GitHub](https://github.com/praza-kembaren) | [Twitter](https://x.com/prazakembaren)""")

with col2:
    file_ = open("/workspaces/portofolio/file/ezgif.com-speed.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(f'<img src="data:image/gif;base64,{data_url}" width="300" height="300" alt="tco gif">',
    unsafe_allow_html=True,)

