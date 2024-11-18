import streamlit as st
import time
import pandas as pd                  
import numpy as np                   
import matplotlib.pyplot as plt      

st.set_page_config(page_title="Earth Similarity Index", page_icon=":earth_africa")


progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.markdown("# Earth Similarity Index (ESI)")
st.markdown("### ESI for Exoplanets")
st.divider()
st.sidebar.header("Earth Similarity Index")
st.sidebar.write("Tugas Mata Kuliah Eksoplanet [AK 3321]")
st.write(
    """"""
)

st.markdown('<div style="text-align: justify;">The Earth Similarity Index is a scale that compare other planets to Earth based on a few physical parameters such as radius, density, escape velocity, and surface temperatureand.  The index ranges from 0 to 1, where a "0" value mean the planet no similarity to Earth and a value "1" mean Earth-like. Planets with an ESI between 0.8 and 1.0 are more likely to be similar to Earth. We can calculated ESI scale for exoplanets with the equation below: </div>', unsafe_allow_html=True)

st.latex(r'''
ESI(S,R) = 1 - \sqrt{\frac{1}{2} \bigg[\bigg(\frac{S-S_\oplus}{S+S_\oplus}\bigg)^2 + \bigg( \frac{R-R_\oplus}{R+R_\oplus}\bigg)^2\bigg]}
    ''')

text = "where $$S$$ is Stellar flux (in Earth unit), $$R$$ stand for Planet's radius, $$S_\oplus$$ is Earth's Solar flux, and $R_\oplus$ is Earth's radius. For the Insolation Flux $S$, the equation is given by:"

st.markdown(f'{text}')
st.latex(r'''
\frac{S}{S_\oplus} = \bigg(\frac{L_*}{L_\odot}\bigg) \bigg( \frac{AU}{a}\bigg)^2
    ''')


url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PS"
st.markdown(f'<div style="text-align: justify;">With these equations and data that was obtained from <a href={url}>NASA Exoplanet Archive </a> We can visualize how similar Exoplanets are to Earth.</div>', unsafe_allow_html=True)

st.link_button("EARTH SIMILARTIY INDEX (ESI) by PHL @ UPR Arecibo", "https://phl.upr.edu/projects/earth-similarity-index-esi")

################################################################################################################################################
st.subheader("Python Code")
code = '''import pandas as pd                  
import numpy as np                   
import matplotlib.pyplot as plt 

df = pd.read_csv("file/exofix3.csv")
df
    '''
st.code(code, language="python")

df = pd.read_csv("file/exofix3.csv")
st.dataframe(df)

#Insolation Flux (S)
S = 10**df['st_lum']*(1/df['pl_orbsmax'])**2

df['st_flu'] = S

code = '''#Insolation Flux (S)
S = 10**df['st_lum']*(1/df['pl_orbsmax'])**2

df['st_flu'] = S
    '''
st.code(code, language="python")

df['a']  = ((df['st_flu'] - 1)/(df['st_flu'] + 1))**2
df['b']  = ((df['pl_rade']- 1)/(df['pl_rade']+ 1))**2
df['esi'] = 1 - np.sqrt(0.5*(df['a'] + df['b']))

code = '''df['a']  = ((df['st_flu'] - 1)/(df['st_flu'] + 1))**2
df['b']  = ((df['pl_rade']- 1)/(df['pl_rade']+ 1))**2
df['esi'] = 1 - np.sqrt(0.5*(df['a'] + df['b']))
    '''
st.code(code, language="python")

st.subheader("Visualization")

code = '''fig, ax =plt.subplots()
ax.scatter( df['st_flu'], df['pl_rade'], s=1)
ax.set_xscale('log')
#plt.ylim(10**-2, 10**2)
#plt.xlim(10**-4, 10**4)
ax.set_yscale('log')
ax.set_xlabel(r"Stellar Flux ($F_{\oplus}$)", fontsize=10)
ax.set_ylabel(r"Planet Radius ($R_{\oplus}$)", fontsize=10)
plt.gca().invert_xaxis()
    '''
st.code(code, language="python")

fig, ax =plt.subplots()
ax.scatter( df['st_flu'], df['pl_rade'], s=1)
ax.set_xscale('log')
#plt.ylim(10**-2, 10**2)
#plt.xlim(10**-4, 10**4)
ax.set_yscale('log')
ax.set_xlabel(r"Stellar Flux ($F_{\oplus}$)", fontsize=10)
ax.set_ylabel(r"Planet Radius ($R_{\oplus}$)", fontsize=10)
plt.gca().invert_xaxis()
ax.set_title("Radius vs Stellar Flux")
st.pyplot(fig)






