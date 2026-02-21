import streamlit as st
import time

st.set_page_config(
    page_title="Happy Birthday Aashita 💖",
    page_icon="🎂",
    layout="centered"
)

# 💗 CSS + JS
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #ffd1dc, #fcbad3);
    overflow: hidden;
    font-family: 'Segoe UI', sans-serif;
}

.heart {
    position: fixed;
    color: #ff4d6d;
    animation: float 6s infinite;
    font-size: 20px;
}

@keyframes float {
    0% { transform: translateY(100vh); opacity: 1; }
    100% { transform: translateY(-10vh); opacity: 0; }
}

.center {
    text-align: center;
}

.title {
    font-size: 50px;
    font-weight: bold;
    color: #7a003c;
}

.subtitle {
    font-size: 20px;
    color: #5a0030;
}

.card {
    background: rgba(255,255,255,0.95);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.2);
}

button[kind="primary"] {
    background-color: #ff4d6d !important;
    border-radius: 25px !important;
    font-size: 18px !important;
}
</style>

<script>
for (let i = 0; i < 25; i++) {
    let heart = document.createElement("div");
    heart.className = "heart";
    heart.innerHTML = "💗";
    heart.style.left = Math.random() * 100 + "vw";
    heart.style.animationDuration = (Math.random() * 3 + 4) + "s";
    document.body.appendChild(heart);
}
</script>
""", unsafe_allow_html=True)

# SESSION STATE
if "started" not in st.session_state:
    st.session_state.started = False

if "yes_clicked" not in st.session_state:
    st.session_state.yes_clicked = False

# 🎉 LANDING SCREEN
if not st.session_state.started:
    st.markdown('<div class="center title">Happy Birthday, Beautiful 💖</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="center subtitle">Today is all about celebrating YOU ✨</div>',
        unsafe_allow_html=True
    )
    st.write("")
    if st.button("🎉 Start the Celebration"):
        st.session_state.started = True
        st.rerun()

# 💌 QUESTION SCREEN
elif not st.session_state.yes_clicked:
    st.markdown('<div class="card center">', unsafe_allow_html=True)
    st.markdown("""
    ### 💭 One Important Question...

    **Aashita, do you know how special you are?** 💗  
    Be honest 👀
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✅ YES"):
            st.session_state.yes_clicked = True
            st.balloons()
            st.rerun()

    with col2:
        st.markdown("""
        <button id="noBtn" style="
            padding: 10px 25px;
            border-radius: 25px;
            border: none;
            background-color: #aaa;
            font-size: 18px;
        ">❌ NO</button>

        <script>
        const btn = document.getElementById("noBtn");
        btn.onmouseover = () => {
            btn.style.position = "absolute";
            btn.style.left = Math.random() * 70 + "%";
            btn.style.top = Math.random() * 70 + "%";
        }
        </script>
        """, unsafe_allow_html=True)

# 💖 EMOTIONAL MESSAGE
else:
    st.markdown('<div class="card center">', unsafe_allow_html=True)
    st.markdown("""
    ### 💌 This is for you, Aashita…

    I hope you always remember this moment.

    You are **deeply appreciated**,  
    **quietly admired**,  
    and **sincerely cared for** 💗  

    Your presence makes days softer  
    and moments warmer ✨  

    Never let the world make you forget  
    how rare and beautiful your heart is 🌸  

    **Happy Birthday. Always stay you.** 🎂💖
    """)
    st.markdown('</div>', unsafe_allow_html=True)
