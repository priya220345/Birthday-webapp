import streamlit as st
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Happy Birthday Aashita 🎉",
    page_icon="🎂",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ffdde1, #ee9ca7);
}
.title {
    text-align: center;
    font-size: 58px;
    font-weight: bold;
    color: #ff4b5c;
}
.subtitle {
    text-align: center;
    font-size: 26px;
    color: #6a0572;
}
.card {
    background: rgba(255,255,255,0.9);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.15);
}
.center {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🎉 Happy Birthday Aashita 🎉</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A little web surprise made just for you ✨</div>', unsafe_allow_html=True)

st.write("")

# Message Card
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("""
### 💖 Dear Aashita,

Today isn’t just your birthday — it’s a celebration of **you** 🌸  

Your smile brings warmth, your kindness leaves a mark,  
and your presence makes ordinary moments special ✨  

May this year bring you:
- 🌈 Joy that stays  
- 🌟 Dreams that come true  
- 💕 Love that grows  
- 🎯 Success that follows you  

Never forget how **special and loved** you are 💫  
Keep shining — the world needs your light 🌍💖
""")
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# Balloons
st.markdown("<div class='center'>🎈🎈🎈🎈🎈🎈🎈</div>", unsafe_allow_html=True)

# Surprise Button
if st.button("🎁 Click for a Surprise"):
    st.balloons()
    with st.spinner("Wrapping happiness... 💝"):
        time.sleep(2)

    st.success("✨ Surprise ✨")
    st.markdown("""
    💌 **Aashita, you are truly one of a kind.**  
    May every day ahead be as beautiful as your heart 💕  
    Happy Birthday once again 🎂🌟
    """)

# Music
st.write("")
st.markdown("### 🎶 Birthday Vibes")
st.audio(
    "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
    format="audio/mp3"
)

# Footer
st.write("")
st.markdown("---")
st.markdown(
    f"<div class='center'>🎂 Made with ❤️ on {datetime.now().strftime('%d %B %Y')} 🎂</div>",
    unsafe_allow_html=True
)
