import streamlit as st

st.set_page_config(page_title="PhishNet AI")

st.title("🚀 PhishNet AI")
st.write("Email Threat Detection System")

email = st.text_area("Enter Email Text")

if st.button("Analyze"):
    if email:
        st.success("App is working ✅")
        st.write("You entered:", email)
    else:
        st.warning("Please enter text")