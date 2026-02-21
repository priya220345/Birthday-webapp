import streamlit as st
import random
import time

st.set_page_config(
    page_title="Happy Birthday Aashita 💖",
    page_icon="🎂",
    layout="centered"
)

# ---------- CSS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom, #ffd1dc, #ffe6ee);
}
h1, h2, h3, p {
    text-align: center;
    color: #5a0033;
}
.box {
    background: #fff0f6;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0 0 15px rgba(255,105,180,0.4);
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("## 💖 💕 💗 💓 💘")
st.markdown("<h1>Happy Birthday, Aashita 🎂</h1>", unsafe_allow_html=True)
st.markdown("<p>Today is all about YOU ✨</p>", unsafe_allow_html=True)

# ---------- WHY SPECIAL ----------
st.markdown("<div class='box'>", unsafe_allow_html=True)
st.markdown("### 💌 Why You’re So Special")
st.write(
    "You have a heart that understands without asking, and a smile that heals without trying. "
    "The world feels softer with you in it 🌸"
)
st.markdown("</div>", unsafe_allow_html=True)

# ---------- OPEN WHEN LETTERS ----------
st.markdown("## 💌 Open When…")

if st.button("Open when you’re happy 😊"):
    st.success("Your happiness makes the world brighter. Never dim that sparkle ✨")

if st.button("Open when you’re sad 🥹"):
    st.info("It’s okay to not be okay. You are loved more than you realize 💕")

if st.button("Open when you miss me 💭"):
    st.warning("Some connections don’t need presence to be felt 💖")

# ---------- COMPLIMENT SHOWER ----------
st.markdown("## 🌸 Compliment Shower")
compliments = [
    "You are effortlessly beautiful 💗",
    "Your kindness is rare and precious ✨",
    "You make people feel seen 🌷",
    "Your presence is comforting 💕",
    "You are enough, always 🤍"
]

if st.button("Give me a compliment 💖"):
    st.success(random.choice(compliments))

# ---------- MOOD SELECTOR ----------
st.markdown("## 🎶 Choose Your Mood")

mood = st.selectbox("How are you feeling right now?", ["Happy 😊", "Emotional 🥹", "Dreamy 🌙"])

if mood == "Happy 😊":
    st.write("Hold onto this feeling — you deserve every bit of joy ✨")
elif mood == "Emotional 🥹":
    st.write("Your sensitivity is your strength, not a weakness 💗")
else:
    st.write("Dream big, beautiful soul. The universe is listening 🌙")

# ---------- WISH GENERATOR ----------
st.markdown("## 🌟 Birthday Wish Generator")

wishes = [
    "May this year bring peace, love, and unexpected happiness 💖",
    "May every quiet wish of your heart come true ✨",
    "May you always feel valued, chosen, and loved 🌸"
]

if st.button("Generate a birthday wish 🎂"):
    st.balloons()
    st.success(random.choice(wishes))

# ---------- MAKE A WISH ----------
st.markdown("## 🕯️ Make a Birthday Wish")
wish = st.text_input("Type your wish here…")

if wish:
    st.write("🤍 Your wish has been sent to the universe.")
    st.write("Sometimes, believing is the first step ✨")

# ---------- SECRET MESSAGE ----------
st.markdown("## 🔐 Secret Message")
code = st.text_input("Enter the secret code")

if code == "AASHITA":
    st.success("You are deeply cherished. More than words can ever explain 💖")

# ---------- SURPRISE ----------
st.markdown("## 🎁 Final Surprise")

if st.button("Start the Celebration 🎉"):
    st.balloons()
    time.sleep(1)
    st.markdown("<h3>May your life be filled with love, light, and laughter 💕</h3>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown("---")
st.markdown("<p>Made with 💖 just for Aashita</p>", unsafe_allow_html=True)
