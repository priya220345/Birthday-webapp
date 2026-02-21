import streamlit as st
import time
from datetime import datetime

st.set_page_config(
    page_title="Happy Birthday Aashita 🎂",
    page_icon="❄️",
    layout="centered"
)

# ❄️ Snowflake animation (CSS + JS)
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #fdeff9, #ec38bc, #7303c0);
    overflow: hidden;
}
.snowflake {
    position: fixed;
    top: -10px;
    z-index: 9999;
    color: white;
    font-size: 1.2em;
    animation: fall linear infinite;
}
@keyframes fall {
    to {
        transform: translateY(110vh);
    }
}
.card {
    background: rgba(255,255,255,0.92);
    padding: 30px;
    border-radius: 22px;
    box-shadow: 0px 15px 40px rgba(0,0,0,0.2);
}
.center {
    text-align: center;
}
.title {
    font-size: 55px;
    font-weight: 800;
    color: #ffffff;
    text-align: center;
}
.subtitle {
    font-size: 22px;
    color: #fcefee;
    text-align: center;
}
</style>

<script>
const snowflakes = Array.from({ length: 40 });
snowflakes.forEach((_, i) => {
  const snow = document.createElement("div");
  snow.className = "snowflake";
  snow.innerHTML = "❄";
  snow.style.left = Math.random() * 100 + "vw";
  snow.style.animationDuration = (Math.random() * 5 + 5) + "s";
  snow.style.fontSize = (Math.random() * 10 + 10) + "px";
  document.body.appendChild(snow);
});
</script>
""", unsafe_allow_html=True)

# 🌸 Title
st.markdown('<div class="title">Happy Birthday Aashita 🎂</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">This page exists only for you ✨</div>', unsafe_allow_html=True)

st.write("")

# 💌 Main Card
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("""
### 💖 Hey Aashita,

If you’re reading this, it means today is **your day** 🌸  
Not just another date — but a reminder of how special you are.

You have this quiet magic about you…  
The kind that makes people feel comfortable, heard, and happy ✨  

This little web page can’t fully express it,  
but it carries one message clearly:

**You matter. A lot.** 💕
""")
st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# 🎁 Surprise 1
if st.button("🎁 Open First Surprise"):
    with st.spinner("Unwrapping something special..."):
        time.sleep(2)
    st.success("🌷 A Wish Just for You")
    st.markdown("""
    May your mornings feel lighter,  
    your nights feel peaceful,  
    and your heart always feel safe where it belongs 💫  

    You deserve a life that feels **soft, exciting, and full** 🌸
    """)

# 🎁 Surprise 2
if st.button("✨ Open Second Surprise"):
    st.balloons()
    st.markdown("""
    🎈 Fun fact about you, Aashita:  
    You make moments memorable without even trying.  
    That’s rare. And beautiful. 💖
    """)

# 🔐 Secret Message
code = st.text_input("🔐 Enter the secret word to unlock something special:")

if code.lower() == "aashita":
    st.markdown("""
    💌 **Secret Message Unlocked**

    Someone made this page because  
    you’re genuinely appreciated —  
    more than you probably realize 🌷  

    Never doubt your worth.  
    Never shrink your light.  
    The world needs *your* version of magic ✨
    """)

# 🎂 Footer
st.write("")
st.markdown("---")
st.markdown(
    f"<div class='center'>Made with ❤️ on {datetime.now().strftime('%d %B %Y')} ❄️🎂</div>",
    unsafe_allow_html=True
)
