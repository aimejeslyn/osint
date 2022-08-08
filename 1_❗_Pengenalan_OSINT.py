# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 00:22:59 2022

@author: user
"""



import streamlit as st
from PIL import Image

#TITLE OF--PAGES
st.title("Mengenal OSINT")


#Apa itu OSINT
st.header("1. Apa itu OSINT?")
st.image("https://itsec.group/img/blog/osint.png")
st.markdown(
            """
        'Open Source' = informasi yang tersedia di ruang publik secara online
        \n'Intelligence' = suatu informasi yang dikumpulkan untuk tujuan analisis data dengan bijak
        \nOSINT sebagai informasi apapun yang dapat dikumpulkan secara legal dari sumber publik yang terbuka secara bebas tentang individu atau organisasi
        \nSebelum adanya internet, sumber daya OSINT dikumpulkan melalui sumber berupa teks seperti surat kabar, gambar, video,webinar, atau pidato publik
        \nSetelah adanya internet sumber informasi OSINT semakin luas, berasal dari data dan informasi yang berada di ranah publik atau terbuka seperti:

                \n1. Media
                \n2. Internet
                \n3. Data Pemerintah Publik
                \n4. Publikasi Profesional dan Akademik
                \n5. Data Komersial
                
            \ndengan ini kita bisa mencari tahu, memprofiling,bahkan mengeksploitasi informasi pribadi seseorang menggunakan internet secara cuma-cuma tanpa harus menguntit/menstalking target yang ingin kita tuju di dunia nyata
    """)
    
#Siapa yang mengendalikan OSINT
with st.container():
   st.write("---")
   st.header("Siapa yang Menggunakan OSINT?")
   st.write("##")
   st.write("OSINT biasa digunakan oleh kalangan profesional seperti")
      
   #membuat gambar dalam 3 kolom
   left_column, center_column, right_column= st.columns(3)
   with left_column:
       st.markdown("1. Cyber Security Professional ")
       st.image("https://insidesources.com/wp-content/uploads/2016/09/AP_110929078944.jpg", caption=('Memantau dan mengidentifikasi peretas'))    
   with center_column:
       st.markdown("2. Petugas penegak hukum ")
       st.image("https://th.bing.com/th/id/OIP.lV8XAbfYymUOOq54JTKrRQHaE7?pid=ImgDet&rs=1", caption=("Mengumpulkan bukti untuk kasus kejahatan"))
   with right_column:
       st.markdown("3. Jurnalis ")
       st.image("https://i.pinimg.com/originals/6e/48/ce/6e48ce40337f0ae8e156632d810cfadb.jpg", caption=("Mengumpulkan informasi tentang suatu objek untuk membantu mereka dalam pelaporan investigasi"))

#SUMBER INFORMASI OSINT
with st.container():
    st.header("Sumber Informasi OSINT")
    st.write("""
             Sumber informasi OSINT:
             - Internet: Forum, blogs, social networking sites(FB, IG, WA), video-sharing sites(Youtube), metadata dan file digital, IP address, people search engine
             - Media massa tradisional: TV, radio, koran, majalah, buku.
             - Data pemerintah publik
             - Publikasi Profesional dan akademik: jurnal, makalah akademik, skripsi
             - Informasi terkait Geospasial: maps


             """)
#Manfaat OSINT
with st.container():
    st.header("Manfaat OSINT")
    st.write("""Bidang OSINT sangat bermanfaat untuk mengidentifikasi dan filterisasi sebuah informasi dengan tujuan tertentu
            \nSemakin bertambahnya pengguna internet dan maraknya kejahatan cyber, Pengumpulan data dari informasi publik untuk mengidentifikasi sebuah kejahatan akan semakin mudah
            \nKarena jumlah sumber terbuka yang tersedia meningkat dengan cepat, melawan kejahatan cyber semakin tergantung pada perangkat lunak canggih dan teknik untuk mengumpulkan dan memproses informasi secara efektif dan efisien, dengan ada nya OSINT ini kita bisa mengurangi dampak kejahatan cyber di era digital saat ini.
            \nMengapa OSINT?
            \n1. Minim resiko
            \n2. Murah
            \n3. Kemudahan aksesibilitas
            \n4. Informasi legal
            \n5. Membantu penyelidikan
            \n6. Menjaga keamanan nasional dan stabilitas politik

                
            """ )
