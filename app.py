import sys
import os
sys.path.append(os.path.abspath("."))

import streamlit as st
from env.environment import PhishNetEnv

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="PhishNet AI",
    page_icon="🛡️",
    layout="centered"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

.main-title {
    font-size: 42px;
    font-weight: bold;
    text-align: center;
    color: #38bdf8;
}

.subtitle {
    text-align: center;
    color: #cbd5f5;
    margin-bottom: 20px;
}

.card {
    background: #1e293b;
    padding: 20px;
    border-radius: 12px;
    margin-top: 15px;
    box-shadow: 0px 0px 10px rgba(56,189,248,0.3);
}

.result-safe {
    color: #22c55e;
    font-size: 28px;
    font-weight: bold;
}

.result-spam {
    color: #facc15;
    font-size: 28px;
    font-weight: bold;
}

.result-phishing {
    color: #ef4444;
    font-size: 28px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.markdown('<div class="main-title">🛡️ PhishNet AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Email Threat Detection System</div>', unsafe_allow_html=True)

# ------------------ INPUT ------------------
email_input = st.text_area("✉️ Enter Email Text", height=150)

# ------------------ BUTTON ------------------
if st.button("🚀 Analyze Email"):

    if email_input.strip() == "":
        st.warning("⚠️ Please enter email text")
    else:
        with st.spinner("Analyzing email... 🔍"):
            env = PhishNetEnv(difficulty="hard")

            env.current_email = {
                "text": email_input,
                "label": "safe"
            }

            state = env._get_state()
            text = state.text.lower()

            # -------- Agent Logic --------
            if "win" in text or "reward" in text:
                action = "spam"
                css_class = "result-spam"
                emoji = "⚠️"
            elif "account" in text or "login" in text:
                action = "phishing"
                css_class = "result-phishing"
                emoji = "🚨"
            else:
                action = "safe"
                css_class = "result-safe"
                emoji = "✅"

        # ------------------ RESULT ------------------
        st.markdown(f"""
        <div class="card">
            <div class="{css_class}">
                {emoji} Prediction: {action.upper()}
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ------------------ FEATURES ------------------
        st.markdown("### 📊 Extracted Features")

        col1, col2, col3 = st.columns(3)

        col1.metric("Length", state.length)
        col2.metric("Has Link", "Yes" if state.has_link else "No")
        col3.metric("Urgent Words", "Yes" if state.has_urgent_words else "No")

# ------------------ FOOTER ------------------
st.markdown("---")
st.markdown("⚡ Built with AI + OpenEnv |")