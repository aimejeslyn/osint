#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 08:58:38 2022

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
st.title("PENERAPAN OSINT")

title_alignment="""
<style>
#penerapan-osint {
  text-align: center;
}
</style>
"""
st.markdown(title_alignment, unsafe_allow_html=True)

#Abstract
st.markdown("""<div style=\"text-align: justify;\">Dalam dunia cybersecurity, 
            OSINT sangat umum digunakan. Berikut adalah dua contoh kasus umum 
            penggunaan OSINT di dunia cybersecurity :</div>""" ,unsafe_allow_html=True)

st.write("\n")
st.write("\n")

with st.expander("Ethical Hacking dan Pengujian Penetrasi"):
    st.markdown("""<div style=\"text-align: justify;\">Para profesional di bidang 
                keamanan siber menggunakan OSINT untuk mengidentifikasi kelemahan 
                pada suatu jaringan sebelum dieksploitasi oleh orang-orang yang 
                tidak bertanggunggjawab. Beberapa kelemahan yang umum ditemukan 
                adalah sebagai berikut :
                </div>""" ,unsafe_allow_html=True)
    st.write("\n")
    
    
    colSpace, colLeft, colRight, colSpace = st.columns([0.2,2,2,0.2], gap='medium')
    with colLeft:
        st.markdown("""<h5 style=\"text-align: center;\">Ketidaksengajaan Membocorkan Informasi yang Sensitif</h5>""",
                    unsafe_allow_html=True)
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSd6dGM2tI5Eij2lk235KOWTw6x2frj-N5t4w&usqp=CAU", caption='Tren Add Yours di Instagram')
        st.markdown("""<div style=\"text-align: justify;\">Contoh ketidaksengajaan meneyebarkan informasi yang sensitif adalah
                               tidak sengaja menyebarkan informasi yang bersifat 
                               pribadi seperti nama panggilan, foto KTP, tanggal 
                               lahir, dan alamat rumah di sosial media seperti Instagram
                               </div>""", unsafe_allow_html=True)
        st.write("\n")
        st.write("\n")
        st.markdown("""<h5 style=\"text-align: center;\">Perangkat Lunak (Software) yang Tidak Ditingkatkan atau Diperbarui Keamanannya</h5>""",
                    unsafe_allow_html=True)
        st.image("https://filestore.community.support.microsoft.com/api/images/b6fbd378-162d-42f5-bab1-aa905bc088f3", caption='Dialog pada Windows XP yang menyatakan bahwa Windows XP sudah tidak dikembangkan lagi setelah tanggal 8 April 2014')
        st.markdown("""<div style=\"text-align: justify;\">Contoh penggunaan sistem operasi yang sudah usang, terlihat pada gambar dialog bahwa Windows XP terakhir kali
                    di-support pada 8 April 2014. Bila kita menggunakan Windows XP pada masa sekarang maka kita berpotensi terkena malware lebih tinggi dibandingkan menggunakan 
                    sistem operasi Windows yang terbaru.</div>""", unsafe_allow_html=True)
        
    with colRight:
        st.markdown("""<h5 style=\"text-align: center;\">Perangkat yang Terkoneksi dengan Jaringan Internet yang Tidak Aman</h5>""",
                    unsafe_allow_html=True)
        st.image("https://1.bp.blogspot.com/-GhX_RTlRrB0/XeS_SEqKh_I/AAAAAAAAHzY/xjvHFShyPcwvencVpi-0d1Qwka8DuM6lgCLcBGAsYHQ/w1200-h630-p-k-no-nu/w1.png", caption='Evil Twin WiFi')
        st.markdown("""<div style=\"text-align: justify;\">Kita harus berhati-hati 
                    jika ingin menggunakan WiFi gratis di ruang publik. Cek terlebih 
                    dahulu apakah perangkat terknoneksi dengan WiFi publik yang asli 
                    atau WiFi publik palsu yang menyerupai WiFi publik yang asli. 
                    WiFi palsu biasanya tidak terdapat proses login dan memiliki koneksi yang lambat.
                    </div>""", unsafe_allow_html=True)
        st.write("\n")
        st.write("\n")
        st.markdown("""<h5 style=\"text-align: center;\">Aset Penting, Seperti Kode Program dari Suatu Aplikasi, yang Bocor ke Khalayak Umum</h5>""",
                    unsafe_allow_html=True)
        st.image("https://images.hothardware.com/contentimages/newsitem/57889/content/lapsus-tweet.jpg", caption='Source code leak dilakukan oleh grup hacker LAPSU$')
        st.markdown("""<div style=\"text-align: justify;\">Contoh kebocoran aset penting adalah seperti 
                    kasus kebocoran source code Samsung yang dilakukan oleh grup hacker LAPSU$. Bila source code 
                    Samsung tersebar di khalayak umum, maka siapapun dapat melihat source code tersebut dan dapat mengeksploitasi kelemahan dari sistem target.
                    Selain itu, peranti lunak yang mengalami kebocoran data akan dipertanyakan kredibilitas 
                    keamanan sistem jaringannya sehingga dapat merugikan perusahaan tersebut.
                               </div>""", unsafe_allow_html=True)
        st.write("\n")
                               
st.write("\n")
with st.expander("Mengidentifikasi Ancaman Eksternal"):
    #animation
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        #animation
        temp_animation=load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_x17ybolp.json")
        st_lottie(
            temp_animation,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",
            height=200,
            width=400,
            key=None,
            )
    st.markdown("""<div style=\"text-align: justify;\">Untuk mengidentifikasi 
                ancaman eksternal, diperlukan seorang analis untuk mengidentifikasi 
                dan mengkorelasikan beberapa data untuk memvalidasi sebuah serangan 
                sebelum serangan tersebut dilakukan. Contoh bila terdapat sebuah cuitan 
                (tweet) ancaman mungkin tidak terlalu mengkhawatirkan, tetapi cuitan 
                tersebut akan menghawatirkan apabila dikirimkan oleh seseorang yang 
                memiliki kaitan dengan suatu kelompok pelaku kejahatan.
                           </div>""", unsafe_allow_html=True)
    st.write("\n")

st.write('---')
st.markdown("**Sumber**")
st.write("https://www.recordedfuture.com/open-source-intelligence-definition")
st.write("Hassan, N. A., &amp; Hijazi, R. (2018). Open source intelligence methods and tools: A practical guide to online intelligence. Apress. ")