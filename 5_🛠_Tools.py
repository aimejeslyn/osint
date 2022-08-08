# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 21:37:37 2022

@author: user
"""
# Forms can be declared using the 'with' syntax
import requests #pip install requests
import streamlit as st 
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie 
from PIL import Image

#LOAD LOTTIER
def load_lottier(url):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#TITLE OF-- TOOLS OSINT
st.title("Tools yang digunakan dalam OSINT?")

#BAGIAN TOOLS 
with st.sidebar:
    selected = option_menu("Tools", ["OSINT Framework", 'Maltego',"Get Contact","Google Dork"], 
        icons=['right', 'right','right','right'], menu_icon="cast", default_index=1)
    selected
#OSINT FRAMEWORK
if selected == "OSINT Framework":
    st.header("OSINT Framework ")
    #LOAD ASSETS
    lottie_coding= load_lottier("https://assets2.lottiefiles.com/packages/lf20_ibujvnor.json")
    left_column, right_column = st.columns(2)
    with left_column:
         st.markdown("""
                     Sebagai pondasi untuk mencari informasi lainnya.
                     Penggunaan framework menfokuskan untuk mengumpulkan informasi dari 
                     sumber dan tools gratis. Fungsinya untuk membantu pengguna menemukan
                     sumber/tools OSINT yang gratis dan mudah ditemukan
                     """)
         st.image("https://miro.medium.com/max/913/1*JuafqtP8G98MKdJrvtKjUg.png")
    with right_column:
         st_lottie(lottie_coding, height=500,key="coding")
         st.subheader("[OSINT Framework>](https://osintframework.com/)")
         
#MALTEGO
if selected== "Maltego":
    st.header("Maltego")
    st.markdown("""
                perangkat lunak yang digunakan untuk open-source intelligence dan forensik
                sumber terbuka, yang dikembangkan oleh Paterva dari Pretoria, Afrika Selatan. 
                \nMaltego berfokus pada penyediaan perpustakaan transformasi untuk penemuan data dari sumber terbuka, 
                dan memvisualisasikan informasi itu dalam format grafik, cocok untuk analisis tautan dan Data mining. 
                """)
    #LOAD ASSETS
    lottie_coding= load_lottier("https://assets5.lottiefiles.com/packages/lf20_bo8vqwyw.json")
    left_column, right_column = st.columns(2)
    with left_column:
         st.image("https://www.silobreaker.com/wp-content/uploads/2020/08/logo-maltego.png")
    with right_column:
         st_lottie(lottie_coding, height=300,key="coding", width=500 )
         st.subheader("[Go to Maltego.com>](https://www.maltego.com/)")

    
#GET CONTACT  
if selected == "Get Contact":
    st.header("Get Contact")
    #LOAD ASSETS
    lottie_coding= load_lottier("https://assets10.lottiefiles.com/packages/lf20_4l3bnj.json")
    left_column, right_column = st.columns(2)
    with left_column:
         st.markdown(""""
                     aplikasi data crowd sourcing yang mana sistem kerjanya 
                     memanfaatkan big data dari user untuk melacak nomor telepon 
                     dan identitas pemilik.
                     """ )
         st.image("https://assets.jalantikus.com/assets/cache/560/350/userfiles/2019/05/20/fungsi-aplikais-get-contact-00aa9.jpg")
    with right_column:
         st_lottie(lottie_coding, height=300,key="coding", width=500 )
         st.subheader("[Get Contact>](https://www.getcontact.com/)")


#GOOGLE DORK
if selected== "Google Dork":
    st.header("Google Dork")
    st.image("https://s3.amazonaws.com/keywordtoolio-blog/wp-content/uploads/2019/05/28125958/Google-Advanced-Search-1024x722.png")
    #LOAD ASSETS
    lottie_coding= load_lottier("https://assets2.lottiefiles.com/packages/lf20_sl6vuo6t.json")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader(" Atau disebut juga Google hacking merupakan versi Advance Google")
        st.write("""
                   Menawarkan fitur pencarian lanjutan yang dapat digunakan oleh pengguna untuk mendapatkan hasil yang lebih spesifik
                    \nKeyword research tools:
                      \n1. Google Keyword Suggest Tool (http://tools.seochat.com/tools/
                                                       suggest-tool): This gives keyword suggestions for Google, Bing, 
                                                        Amazon, and YouTube.
                      \n2. Google AdWords (https://adwords.google.com/home/tools/
                                           keyword-planner/) and Google Trends (https://www.google.com/
                                                                                trends): These will show search volume and matrices of Google 
                                                                                searches for any geographical region in the entire world.
                      \n3. One Look 
                      (www.onelook.com/reverse-dictionary.shtml): Enter a 
                          word, phrase, sentence, or pattern to search for related words
                    """ )
    with right_column:
         st_lottie(lottie_coding, height=300,key="coding", width=300 )
         st.subheader("[Go to Advance Search>](https://www.google.com/advanced_search)")  
else:
    ""



