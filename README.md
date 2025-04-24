# Rastgele-Sifre-Uretici-ile-Streamlit-Projesi
Giriş

Güvenli şifreler oluşturmak, dijital dünyada hesaplarımızı korumak için vazgeçilmezdir. Bu projede Python dili ve Streamlit kütüphanesi kullanarak, hem özelleştirilebilir hem de modern bir web arayüzüne sahip bir şifre üretici geliştireceğiz.

Proje Amacı

Kullanıcıya:

Şifre uzunluğunu seçebilme,

Hangi karakter gruplarını kullanacağına karar verme,

Renkli ve okunabilir bir arayüzde sonuç gösterimi
sunar.

Kullanılan Araçlar

Python 3.x

Streamlit: Hızlı ve kolay arayüz geliştirme

HTML: Gelişmiş stil ve renk desteği

random: Rastgele karakter seçimi

Uygulamanın Adımları

1. Gerekli Kütüphaneleri Çağırma
import streamlit as st
import html
import random

2. Başlık ve Tanıtım
   
st.markdown("<h1 style='font-size:22px;'>🔐 Rastgele Şifre Üretici</h1>", unsafe_allow_html=True)

4. Kullanıcıdan Girdi Alma

Kullanıcıdan şu bilgiler alınır:

Şifre uzunluğu (6-100)

Karakter tipleri (küçük, büyük harf, rakam, özel karakter)

length = st.number_input("Şifre Uzunluğunu Girin", min_value=6, max_value=100, value=15, step=1)

4. Karakter Havuzu

Seçilen karakter türlerine göre havuz oluşturulur:
character_pool = ""
if use_lowercase:
    character_pool += lowercase
 ... devam eder

5. Şifre Üretme ve Gösterim

Butona tıklandığında rastgele şifre oluşturulur. Seçimler uygun değilse uyarı verilir.
if st.button("🎲 Şifre Oluştur"):
    if len(character_pool) == 0:
        st.error("Lütfen en az bir karakter grubu seçin!")

Sonuç, HTML ile görsel olarak zenginleştirilir:
st.markdown(f"""
<p style='font-size:32px;'>
    <span style='color:black;'>Yeni Şifre: </span>
    <code style='color:red;'>{safe_password}</code>
</p>
""", unsafe_allow_html=True)

Kullanıcı Deneyimi

Kullanıcılar bu uygulamada:

Çekici ve basit arayüz sayesinde kolayca etkileşim kurar.

Anlık olarak şifreyi görebilir.

Güvenli, karmaşık şifreleri saniyeler içinde elde eder.

Bu mini proje, hem frontend hem de backend bìrleşimini içeren, pratik bir Streamlit uygulaması olarak tasarlanarak hayata geçirilmiştir.
