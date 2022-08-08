#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 10:50:59 2022

@author: El
"""
#lib
import streamlit as st
import requests
from streamlit_lottie import st_lottie

#Load animation 
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Title
st.title("METODE OSINT")

title_alignment="""
<style>
#metode-osint {
  text-align: center;
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

#Abstract
st.markdown("""<div style=\"text-align: justify;\"> Sumber OSINT dapat dikumpulkan 
             melalui 3 metode utama, yaitu Passive, Semipassive, dan Active. 
             Metode OSINT yang akan digunakan bergantung pada proses pengambilan 
             data apa yang ingin dicari. Ketiga metode OSINT ini secara umum 
             digunakan untuk mengumpulkan informasi infrasturktur IT yang 
             ditarget. Berikut adalah penjelasan ketiga mode OSINT :</div>""" ,unsafe_allow_html=True)
st.write("\n")
st.write("\n")

with st.expander("Passive Collection"):
    #layout
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        #animation
        temp_animation=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_l5qvxwtf.json")
        st_lottie(
            temp_animation,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=150,
            width=390,
            key=None,
            )
    #text
    st.markdown("""<div style=\"text-align: justify;\"> Passive collection 
                merupakan metode OSINT paling sering digunakan karena metode 
                Passive collection hanya mengumpulkan informasi melalui sumber 
                yang ada secara publik. Dengan menggunakan metode ini, target 
                anda tidak akan mengetahui proses pengumpulan informasi yang 
                anda lakukan. Namun, informasi yang anda dapatkan sangatlah terbatas 
                dan sumber utama yang anda gunakan biasanya merupakan informasi 
                yang sudah tidak relevan, data yang tidak terlindungi pada server, 
                dan konten yang ada pada website target anda.</div>""" ,unsafe_allow_html=True)
st.write("\n")
with st.expander("Semipassive Collection"):
    #layout
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        #animation
        temp_animation=load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_lo53sxhu.json")
        st_lottie(
            temp_animation,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=150,
            width=390,
            key=None,
            )
    st.markdown("""<div style=\"text-align: justify;\"> Metode semipassive dilakukan dengan cara mengirimkan trafik pada 
    server target untuk memperoleh informasi umum tentang target. Trafik 
    ini harus menyerupai trafik internet pada umumnya untuk menghindari 
    kecurigaan saat melakukan pengintaian.  Dengan metode ini, Anda hanya 
    melakukan investigasi yang tidak terlalu mendalam tanpa menimbulkan 
    kecurigaan dari target Anda.</div>""" ,unsafe_allow_html=True)

st.write("\n")
with st.expander("Active Collection"):
    #layout
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        #animation
        temp_animation=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_87edm6kj.json")
        st_lottie(
            temp_animation,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=150,
            width=390,
            key=None,
            )
    st.markdown("""<div style=\"text-align: justify;\"> Pengumpulan informasi dengan metode active dapat dilakukan dengan 
        cara secara langsung berinteraksi dengan sistem target. Namun dengan 
        menggunakan metode ini, target anda dapat menyadari proses pengintaian 
        karena anda atau seseorang yang melakukan pengumpulan informasi akan 
        menggunakan teknik yang lebih canggih untuk mengambil data tentang 
        infrastruktur IT target seperti mengakses port terbuka, memindai 
        kerentanan, memindai aplikasi web server, dan lain-lain. Trafik ini 
        akan terlihat seperti aktivitas yang mencurigakan dan dapat meninggalkan 
        jejak pada sistem deteksi intrusi (IDS) target atau sistem pencegahan 
        intrusi (IPS) target. Social engineering attacksjuga termasuk dalam 
        metode pengumpulan informasi secara active.</div>""" ,unsafe_allow_html=True)

st.write('---')
st.markdown("**Sumber**")
st.write("https://www.recordedfuture.com/open-source-intelligence-definition")
st.write("Hassan, N. A., &amp; Hijazi, R. (2018). Open source intelligence methods and tools: A practical guide to online intelligence. Apress. ")
