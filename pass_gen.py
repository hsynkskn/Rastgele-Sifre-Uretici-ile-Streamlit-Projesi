import streamlit as st
import html
import random

# Başlık
st.markdown("<h1 style='font-size:22px;'>🔐 Rastgele Şifre Üretici</h1>", unsafe_allow_html=True)

st.markdown("""
<p style='font-size:16px'>
Bu araç sayesinde özel, güvenli ve rastgele şifreler oluşturabilirsiniz.
</p>
""", unsafe_allow_html=True)

# Kullanıcıdan şifre uzunluğu alınır
length = st.number_input("Şifre Uzunluğunu Girin", min_value=6, max_value=100, value=15, step=1)

use_lowercase = st.checkbox("Küçük Harf (a-z)", value=True)
use_uppercase = st.checkbox("Büyük Harf (A-Z)", value=True)
use_digits = st.checkbox("Rakamlar (0-9)", value=True)
use_special = st.checkbox("Özel Karakterler (!,^,+,%,&,...)", value=True)

# Karakter kümeleri
lowercase = "abcdefghijklmnoqprstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOQPRSTUVWXYZ"
digits = "1234567890"
special = "!'^+%&/()=?_-+*/<>.,@"

# Kullanıcıya bağlı olarak havuz oluştur
character_pool = ""
if use_lowercase:
    character_pool += lowercase
if use_uppercase:
    character_pool += uppercase
if use_digits:
    character_pool += digits
if use_special:
    character_pool += special

# Şifre üretme butonu
if st.button("🎲 Şifre Oluştur"):
    if len(character_pool) == 0:
        st.error("Lütfen en az bir karakter grubu seçin!")
    elif length > len(character_pool):
        st.warning("Uyarı: Seçilen karakter havuzu, şifre uzunluğundan kısa. Karakterler tekrar edebilir.")
        password = ''.join(random.choices(character_pool, k=int(length)))
    else:
        password = ''.join(random.sample(character_pool, int(length)))

    # Şifreyi HTML uyumlu hâle getiriyoruz
    safe_password = html.escape(password)

    st.markdown(
    f"""
    <p style='font-size:28px;'>
        <span style='color:green;'>Yeni Şifre: </span>
        <code style='color:red;'>{safe_password}</code>
    </p>
    """,
    unsafe_allow_html=True
)
