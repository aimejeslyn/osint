#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 18:44:44 2022

@author: El
"""

#library
import streamlit as st

st.title("SISI GELAP OSINT")
title_alignment="""
<style>
#sisi-gelap-osint{
  text-align: center;
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

#Abstract
c1, c2, c3 = st.columns(3)
with c2 :
    st.write("![Your Awsome GIF](https://c.tenor.com/YNQlVZi09jcAAAAC/darth-vader-power.gif)")
st.markdown("""<div style=\"text-align: justify;\"> OSINT memang sangatlah 
            bermanfaat bagi analisis kemanan siber, tetapi OSINT menjadi 
            berbahaya apabila digunakan oleh para pelaku kejahatan (threat actors). 
            Para pelaku kejahatan dapat menggunakan OSINT untuk mengidentfikasi 
            target dan mengeksploitasi kelemahan jaringan target. Saat kelemahan 
            target teridentifikasi, maka para pelaku kejahatan akan dengan cepat 
            mengeksploitasi jaringan tersebut. Hal ini selalu terjadi pada 
            perusahan kecil dan menengah setiap tahunnya karena sistem keamanan 
            jaringan atau arsitektur website yang lemah sehingga mudah ditemukan
            kelemahan melalui menggunakan teknik OSINT saja. Selain itu, para 
            pelaku kejahatan dapat mencari informasi tentang suatu individu dan 
            organizasi yang dapat digunakan untuk melakukan social engineering 
            seperti phising (melalui surel), vishing (melalui telepon), dan 
            SMiShing (melalui SMS). Seringkali, para pelaku kejahatan 
            mengirimkan suatu informasi yang telihat tidak berbahaya dan 
            terlihat terpercaya yang digunakan untuk mengelabui para target
            agar para pelaku kejahatan dapat mengakses jaringan atau aset 
            target.</div>""" ,unsafe_allow_html=True)

st.write('---')
st.markdown("**Sumber**")
st.write("https://www.recordedfuture.com/open-source-intelligence-definition")
st.write("Hassan, N. A., &amp; Hijazi, R. (2018). Open source intelligence methods and tools: A practical guide to online intelligence. Apress. ")