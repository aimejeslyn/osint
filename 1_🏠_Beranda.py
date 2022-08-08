#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 20:57:39 2022

@author: El
"""
import streamlit as st
import requests
from streamlit_lottie import st_lottie


#PAGE NAME

#Load animation 
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    
#inject local CSS buat bikin contact form
def local_css(file_name):
    with open(file_name)as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

lottie_coding= load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_r81jI1.json")

st.title("Mari Berkenalan dengan OSINT!")
st.write("\n")
st.write("\n")
    
        
temp_animation=load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_96bovdur.json")
st_lottie(
        temp_animation,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height=600,
        width=400,
        
        )

if st.button("Mulai!"):
    st.balloons()
    
    #HEADER SECTION
    st.title("Hello, We are Team 1 : :wave:")
    st.title("Women in OSINT ")
    st.subheader("Team of two members:")
    st.write("1. Aime Jeslyn S.", "\n2. Elsy Sabrina R.")


    #BIODATA
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("What We do")
            st.write("##")
            st.write(
                """
                Pada presentasi hari ini, Team kami akan membahas hal-hal berkaitan tentang OSINT:
                - Definisi OSINT
                - Manfaat OSINT
                - Sumber informasi OSINT
                - Pengguna OSINT
                - Metode OSINT
                - Penerapan OSINT
                - Sisi Gelap OSINT
                - Tools OSINT
                - Kasus berkaitan dengan OSINT
                """)
        with right_column:
            st_lottie(lottie_coding, height=500,key="coding")

    #CONTACT INFORMATION
    with st.container():
        st.write("---")
        st.header("Get in Touch With Us!")
        st.write("##")
        
        #Link: https://formsubmit.co/
        contact_form= """
        <form action="https://formsubmit.co/aimejeslyns@outlook.com" method="POST"> 
         <input type="hidden" name="_captcha" value="false">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <input type="message name="message" placeholder="Your message here" required>
         <button type="submit">Send</button>
    </form>
    """
    #dibuat menjadi column 
        left_column, right_column= st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()


