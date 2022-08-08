# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 00:31:29 2022

@author: user
"""

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

#sidebar menuS
with st.sidebar:
    selected = option_menu("Case Study", ["Case 1", 'Case 2','Case 3'], 
        icons=['book', 'book-half','book-fill'], 
        menu_icon="cast", default_index=0)   
    selected

#selection

#CASE 1--PEMBAKARAN HALTE SASRINAH
if selected == "Case 1":
    st.header("62 Menit Operasi Pembakaran Halte Sarinah")
    st.write("""
             Pada Kamis, 8 Oktober 2020 terjadi demonstrasi menolak Undang-Undang Cipta Kerja terjadi 
             serempak pada beberapa kota di Indonesia. Seperti yang sudah disiarkan di berita, ada beberapa 
             fasilitas umum dirusak. Jalan Thamrin hingga Sudirman lokasi kumpul massa jadi sorotan utama. 
             Beberapa halte Transjakarta dibakar seperti halte Bundaran HI, Sarinah, dan Tosari. 
             Para demonstran dikritik bahkan dituduh sebagai pelaku perusakan, tetapi pertanyaan yang menjadi 
             kontrovesial adalah apakah benar para demostran yang membakar halte di Sarinah? Laporan yang dibuat 
             oleh tim Narasi Newsroom disusun dengan menganalisis visual dari berbagai open source. Mereka juga memakai 
             rekaman CCTV dari lokasi kejadian yang bisa diakses publik secara bebas. Selain itu, mereka mengumpulkan
             ratusan foto dan video yang tersebar bebas di Instagram, Twitter, Youtube, dan Tiktok. Berdasarkan sumber
             yang ada, kita jadi paham apa yang sebenarnya terjadi di Sarinah pada sore itu.
             """)
    st.image('http://student-activity.binus.ac.id/csc/wp-content/uploads/sites/37/2022/04/image16.png')
    st.image("http://student-activity.binus.ac.id/csc/wp-content/uploads/sites/37/2022/04/image4.png")
    st.image('http://student-activity.binus.ac.id/csc/wp-content/uploads/sites/37/2022/04/image12.png')
    
    st.write("""Orang misterius ini lah yang pertama menyulut api di Halte Sarinah. 
                 Potongan video tiktok di bawah ini diambil pukul 16:39. Dua video ini memperlihatkan 
                 api belum terlihat di Halte Sarinah, tetapi api ini yang akan dijadikan sumber oleh pelaku 
                 untuk membakar Halte.""")
    st.image('http://student-activity.binus.ac.id/csc/wp-content/uploads/sites/37/2022/04/image11.png')
    st.image('http://student-activity.binus.ac.id/csc/wp-content/uploads/sites/37/2022/04/image7.png', caption="saat api belum terlihat di Halte Sakinah")
    st.image('http://student-activity.binus.ac.id/csc/wp-content/uploads/sites/37/2022/04/image10.png', caption=("Jika kamu melihat ada asap di atas halte, itu bukan berasal dari halte tersebut"))
    st.write('''Keempat orang yg dilingkari menjadi potensi sebagai pelaku pembakaran, 
             terlihat mereka mengenal satu sama lain. Mereka bergerombol datang pada 
             pukul 16:41 dari arah jalan Sunda. Mereka tidak langsung beraksi, para pelaku melakukan observasi
             terlebih dahulu selama beberapa menit.
             ''')
    st.image('http://student-activity.binus.ac.id/csc/wp-content/uploads/sites/37/2022/04/image8.png',)
    st.image('http://student-activity.binus.ac.id/csc/wp-content/uploads/sites/37/2022/04/image9.png')
    st.write('''Pada menit 16:45, pelaku mendekat ke Halte Sarinah. Sebelumnya, ia sempat berkomunikasi 
             dengan temannya dan menunjuk ke arah kobaran api yang akan dijadikan sumber untuk membakar Halte Sarinah.''')
    left_column, right_column= st.columns(2)
    with left_column:
        st.image('http://student-activity.binus.ac.id/csc/wp-content/uploads/sites/37/2022/04/image15.png')
    with right_column:
        st.image('http://student-activity.binus.ac.id/csc/wp-content/uploads/sites/37/2022/04/image13.png')
    
    st.write('Dengan machine learning berbasis tensorflow, kita bisa sedikit memperjelas wajah si pelaku utama dan rekannya. Hasilnya seperti ini.')
    st.image('http://student-activity.binus.ac.id/csc/wp-content/uploads/sites/37/2022/04/image14.png')
    
    st.write("[Sumber referensi>](https://student-activity.binus.ac.id/csc/2022/04/open-source-intelligence-osint/)")
    
#RUSSIAN GIRL TIED UP AS LIVING SHIELD
if selected == 'Case 2':
    st.header('A Russian girl tied up as a living shield by Ukrainian soldiers in Mariupol')
    st.image('https://pbs.twimg.com/media/FPL8FoFXwAUpxEU?format=jpg&name=large')
    
    st.write('Upload screenshots ke Russian search engine Yandex.com ')
    st.image('https://pbs.twimg.com/media/FPL9UfCWUAUuhrf?format=jpg&name=medium')
    
    st.write('Hasil pencarian membawa kita menuju post dari 21 Maret 2022, terlihat juga foto yang menyerupai')
    st.image('https://pbs.twimg.com/media/FPL9f2pWUAEL6zV?format=jpg&name=small')
    st.write('Foto yang menyerupai juga dibagikan oleh Jurnalis asal Jerman')
    st.image('https://pbs.twimg.com/media/FOdPjg6XMAE1rX3?format=jpg&name=large')
    
    st.write('Kita telusuri lebih dalam lagi menggunakan Google search engine')
    st.image('https://pbs.twimg.com/media/FPL-nphXsAMyoYv?format=jpg&name=900x900')
    st.write("""Kami menemukan artikel ini dari @romeanews, media berita yang berfokus 
             pada komunitas Roma. Artikel 'Rusia mendistorsi foto untuk tujuan propaganda,
             organisasi nirlaba Roma memperingatkan pihak berwenang Ukraina' menunjukkan 
             foto-foto yang diselidiki sebagai ilustrasi.
             \nMenurut artikel tersebut, foto-foto tersebut menunjukkan Roma di Lviv. 
             Mereka diduga adalah penjambret dompet yang ketahuan menjarah di Lviv 
             kemudian dihukum dan dipermalukan dengan cara yang mengerikan ini.
             \nMenurut @romeanewsada "sebuah kelompok di Lviv yang menyebut dirinya 'The Hunters' yang menuntut Roma yang terlibat dalam pencopetan".
             Apakah kelompok 'The Hunters' ini bertanggung jawab atas kebencian 
             terhadap Roma ini?
             \nOrganisasi hak asasi manusia Ukraina @zminaUkraine menulis tentang The Hunters 
             pada awal 2021 ketika seorang Roma, yang dicurigai mencuri, terpaksa merangkak dengan tangan dan lututnya dan dipukuli. 
             'Vigilante Group' didirikan pada tahun 2018 (link= "https://t.co/fH1PAOkRWO")
             \nGrup publik di Facebook, The Hunters online pada 23 Januari 2018. 
             Bahkan kemudian, Zmina menulis tentang fenomena tersebut, yang merupakan bagian dari kekerasan 
             sebelumnya terhadap orang Roma di wilayah tersebut.
             """)
    st.image('https://pbs.twimg.com/media/FPMBAJvXsAU_PW3?format=jpg&name=900x900')
    
    st.write("Seorang anggota The Hunters juga membagikan artikel berita dari media Ukraina Varta1 berjudul 'In Lviv, hunted and tied to a pole'(link='https://t.co/oXvWwIQON2')")
    st.image('https://pbs.twimg.com/media/FPMBb8PXEAcvQXr?format=jpg&name=small')
    
    st.write('Artikel ini membantu kami menemukan lokasi gambar. Persimpangan utara Lviv di Google Streetview (kiri) cocok dengan salah satu foto (kanan). Kami melihat tenda minuman yang sama dan pompa bensin yang sama di latar belakang')
    st.image('https://pbs.twimg.com/media/FPMCAUUXEAAPhya?format=jpg&name=large')
    
    st.write("""
             Tidak semua elemen cocok, karena foto Streetview berasal dari Juli 2015. 
             Bangunan yang saat itu sedang dibangun selesai dibangun pada 21 Maret 2022. 
             Tiang tempat gadis itu diikat belum ada di sana pada tahun 2015.
             \nKembali ke The Hunters.Orang-orang tertentu mana yang bertanggung jawab 
             yang tidak dapat kita temukan, tetapi tampaknya pasti bahwa The Hunters 
             terlibat. 
             \nMengapa?
             \nMereka tidak hanya berbagi foto yang tidak dapat kami temukan di tempat lain, tetapi administrator grup juga memposting video pendek pada 11 Maret. 
             Ini menunjukkan lima gadis dan wanita muda dengan wajah dan tangan dicat 
             hijau lagi. Beberapa dari mereka bahkan disebutkan dengan nama dan tanggal lahir. 
             \nWarna hijau pada tersangka pencuri terutama tangan dan wajah lebih sering diwwarnai hijau. 
             Ini adalah zelyonka, pewarna antiseptik yang sulit dihilangkan pada kulit(link=https://t.co/kkJVzPLZXt).
             """)
    st.image('https://pbs.twimg.com/card_img/1553586958009602048/TWFpnqIF?format=jpg&name=900x900')
    
    st.write('menganalisis lebih dalam dengan gambar yang serupa: "Di Ukraina warga saat ini sedang diikat ke tiang dan dipukuli. Selain itu, gambar-gambar ini sedang dieksploitasi sepenuhnya - dan sebagian disalahartikan - oleh kubu Rusia dalam perang informasi."')
    st.image('https://pbs.twimg.com/card_img/1552845928234717188/p7GYvklR?format=jpg&name=900x900',caption=('https://t.co/foKeZ5vUo1'))
    
    st.write("Gambar-gambar 21 Maret di Lviv juga muncul di penyiar negara Rusia RT. Artikel itu membuat tautan dengan apa yang disebut 'denazifikasi' Ukraina. Rusia mengeksploitasi ini untuk menuduh Ukraina dijalankan oleh neo-Nazi")
    st.image('https://pbs.twimg.com/media/FPMFSxtXMAgj4sS?format=jpg&name=medium')
    
    st.subheader('Kesimpulan')
    st.write("""Foto yang beredar tidak menunjukkan 'seorang gadis Rusia
             diikat sebagai perisai hidup di Mariupol. 
             Ini adalah serangan publik untuk tersangka pencuri di Lviv. Menurut berbagai sumber, mereka adalah orang Roma. 
             Gambar-gambar tersebut digunakan oleh propaganda Rusia.""")
    st.write("[Sumber referensi>]('https://t.co/osSrl0ATxC')")

#KIM KARDASHIAN INVESTIGATION
if selected == 'Case 3':
    st.header("How Dare You?: Kim Kardashian’s 40th Birthday, An Investigation")
    st.write("""
             Pada saat liburan, Kim Kardashian membuat video di twitternya.
             \nVideo tersebut mencakup foto-foto keluarga dan berbagai macam gantungan baju 
             yang memainkan Uno, kursi ember mewah di pesawat, dan bidikan situasi 
             Kris Jenner Corey Gamble yang memotongnya di dekat bar/area sosial di pesawat.
             Dan maukah Anda melihat itu? Ada semacam logo di bagian depan bilah tersebut. 
             Saya memakai Kacamata Pembesar Jurnalis saya, mengambil tangkapan layar dan 
             menemukan gambar dua kuda laut yang dipisahkan oleh busur permata. 
             """)
    st.image('https://miro.medium.com/max/456/1*_3JuidmnKpZv1xkPEZrrvw.png')
    st.write("""
             Pencarian Google Image Reverse menemukan bahwa logo tersebut 
             milik Crystal Cruises, sebuah perusahaan kapal pesiar yang memiliki 
             divisi jet sewaan bernama Crystal Aircruises. 
             (Terlihat, jet sewaan tidak memiliki cincin yang sama.) 
             Jet itu adalah Boeing-777 yang disebut Crystal Skye.
             \nSetelah ditelusuri nama pesawat itu adalah P4-XTL. Bagaimanapun, P4-XTL adalah jet 
             wisata pribadi terbesar di dunia dan penerbangan tersebut tidak
             mungkin menuju ke sembarang tempat.
             \nMenurut FlightRadar24, P4-XTL baru-baru ini terbang antara LAX, 
             bandara pilihan keluarga Kardashian, dan Pape'ete, ibu kota Polinesia Prancis. 
             Kecuali ini adalah tipuan yang sangat mahal, Kim kemungkinan menghabiskan 
             ulang tahunnya yang ke-40 di Polinesia Prancis.
             """)
    st.image('https://miro.medium.com/max/1400/1*JKje8P3GoXnIjNWD2PklnQ.png')
    st.write("""
             Hasil yang pertama kali muncul pada Google Search adalah 
             'pulau pribadi Polinesia Prancis' adalah sebuah resor bernama The Brando yang 
             berada di Teti'aroa, sebuah atol yang pernah dimiliki oleh aktor dan gadis 
             video musik Marlon Brando, Itu juga menjamu Barack Obama yang
             pergi ke sana tepat setelah pelantikan selama sebulan untuk menulis memoarnya.
             \nDi setiap lingkaran pertemanan, pasti ada yang secara tidak 
             sengaja mem-posting hal yang krusial. 
             Dalam kru yang terdiri dari empat puluh orang ini, model dan saudara perempuan 
             Kardashian Kendall Jenner yang memposting video dari bar luar ruangan di hotel. 
             (Keterangan: "lokasi rahasia." Berkatilah.) Orang lain telah membantu mengunjungi 
             bar di Brando dan mengambil foto Google Street View.
             \nTampaknya, mereka duduk di kursi yang sama persis dengan Kendall karena 
             pandangannya terlihat persis seperti pemandangan dari bar di The Brando.
             Tetapi jika Anda belum pernah ke daerah tropis, banyak
             bar pulau memiliki atap rumput yang menghadap ke pantai.
             """)
    st.image('https://miro.medium.com/max/1400/1*Y8maLorgoLqzvgBG5XUzfg.png')
    st.image('https://miro.medium.com/max/1400/1*ZCaEbbfeTfMXVqXBhl_nbw.png')
    st.write("""Terlihat di post-nya Kendall membagikan lagi. Kali ini, cermin kamar mandi 
             yang menarik perhatian Vicky. Ini adalah cermin bundar dengan backsplash batu 
             bertekstur, 
             yang dimiliki banyak kamar mandi di The Brando.
             """)
    st.image('https://miro.medium.com/max/1000/1*CDZCsdglaR72xAd461XNRA.png')
    st.write("""
             Keterangan Insta Kim menyebutkan bahwa mereka "mengendarai sepeda." , 
             informan wanita yang bekerja dengan Kenddal mengkonfirmasikan bahwa Instagram
             Story itu adalah 'mereka'.
             Yang terlihat cukup mirip dengan foto Instagram yang diposting 
             silang ke situs web Brando. Tidak hanya itu. Saya bukan ahli pohon tetapi 
             dedaunan juga cocok.
             \nDalam satu foto, Kim berdiri di depan beberapa tangga sementara demgan  
             latar belakang Kris dan Corey.
             Semuanya terlihat biasa tetapi bagian yang paling
             menarik adalah eksterior kayu di sebelah kiri foto yang cocok dengan eksterior 
             tempat tinggal utama di pulau itu, tempat yang memungkinkan Google Maps dan resor
             anda lewati.
             """)
    left_column, right_column= st.columns(2)
    with left_column:
        st.image('https://pbs.twimg.com/media/ElWsBzPXYAIyhFd?format=jpg&name=large')
    with right_column:
        st.image('https://pbs.twimg.com/media/ElWsBzaWoAALW1U?format=jpg&name=large')
        st.write("[Kim Kardashian tweet>](https://twitter.com/KimKardashian/status/1321151217482014726?ref_src=twsrc%5Etfw%7Ctwcamp%5Etweetembed%7Ctwterm%5E1321151224889151490%7Ctwgr%5E6a7c38f7d3617564e22432a29371c2b5c1fa624b%7Ctwcon%5Es2_&ref_url=https%3A%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Ftype%3Dtext2Fhtmlkey%3Da19fcc184b9711e1b4764040d3dc5c07schema%3Dtwitterurl%3Dhttps3A%2F%2Ftwitter.com%2Fkimkardashian%2Fstatus%2F1321151224889151490image%3D)")
     
    left_column, right_column= st.columns(2)
    with left_column:
          st.image('https://pbs.twimg.com/media/ElWsCPdXIAch07O?format=jpg&name=small')
          
    with right_column:
          st.image('https://pbs.twimg.com/media/ElWsCQSW0AIk1Kx?format=jpg&name=small')
    
    st.image('https://miro.medium.com/max/1400/1*vuBMF4wf5aeiAPdsNZ2pzQ.png')
    st.write("""Kesimpulan:
             \nDari penjelasan tersebut kita ketahui bahwa acara ulang tahun Kim Kardashian 
             dimeriahkan di Resort The Brando yang terletak di French Polynesia di pulau Tetiaroa.
             Walaupun Kim sebagai selebritas papan atas berusaha menyembunyikan lokasi tempat tapi juga
             berusaha untuk tetap eksis, sama saja tetap akan terlacak lokasinya, ditambahkan juga beberapa
             orang/anggota keluarga ada yang tidak berhati-hati dalam membagikan post. Dengan begitu 
             lokasi sangat mudah untuk terlacak hanya dengan menggunakan Google Lens dan Google maps.
             """)
    st.markdown("[Sumber referensi:>](https://vickymochama.medium.com/how-dare-you-kim-kardashians-40th-birthday-an-investigation-766dc879eb23)") 