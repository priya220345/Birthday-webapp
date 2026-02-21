import streamlit as st
import random
import time

# ---------- Page Config ----------
st.set_page_config(
    page_title="Happy Birthday Aashita 💖",
    page_icon="🎂",
    layout="centered"
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #ffd1dc, #ffe6ee);
}
.main {
    background-color: transparent;
}
h1, h2, h3, p {
    text-align: center;
    color: #5a0033;
}
.heart {
    font-size: 28px;
    animation: float 3s infinite;
}
@keyframes float {
    0% {transform: translateY(0);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0);}
}
.special-box {
    background: #fff0f6;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 0 15px rgba(255, 105, 180, 0.4);
}
</style>
""", unsafe_allow_html=True)

# ---------- Floating Hearts ----------
hearts = "💖 💕 💗 💓 💘"
st.markdown(f"<h3 class='heart'>{hearts}</h3>", unsafe_allow_html=True)

# ---------- Hero Section ----------
st.markdown("<h1>Happy Birthday, Aashita! 🎂✨</h1>", unsafe_allow_html=True)
st.markdown(
    "<p>Today is all about celebrating <b>YOU</b> and the happiness you bring into the world 💗</p>",
    unsafe_allow_html=True
)

st.write("")

# ---------- Special Message ----------
with st.container():
    st.markdown("<div class='special-box'>", unsafe_allow_html=True)
    st.markdown("### 💌 Why You’re So Special")
    st.write(
        "You have this beautiful way of making people feel warm, understood, and valued. "
        "Your smile carries comfort, and your presence feels like home. 🌸"
    )
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# ---------- Memory Lane ----------
st.markdown("## 🌷 Memory Lane")
memories = [
    "Your kindness is your superpower 💫",
    "You light up every room you walk into ✨",
    "Your laugh makes bad days better 🌈",
    "You deserve all the love today and always 💕"
]

if st.button("Tap to reveal a memory 💭"):
    st.success(random.choice(memories))

st.write("")

# ---------- Surprise Section ----------
st.markdown("## 🎁 A Little Surprise")

if st.button("Open your surprise 🎀"):
    st.balloons()
    time.sleep(1)
    st.markdown(
        "<h3>May this year give you everything your heart quietly wishes for 💖</h3>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p>Never forget how deeply loved and appreciated you are.</p>",
        unsafe_allow_html=True
    )

st.write("")

# ---------- Footer ----------
st.markdown("---")
st.markdown(
    "<p>Made with 💕 just for you, Aashita</p>",
    unsafe_allow_html=True
)
