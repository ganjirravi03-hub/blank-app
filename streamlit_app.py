
import streamlit as st
import pandas as pd
from openai import OpenAI

# 🔐 Secure API Key
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="AI Assistant", layout="centered")

st.title("🤖 AI Smart Assistant")
st.write("Chat + File Analysis System 🚀")

# =========================
# 📂 FILE UPLOAD
# =========================
uploaded_file = st.file_uploader("Upload CSV or TXT", type=["csv", "txt"])

file_content = ""

if uploaded_file:
    if uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())
        file_content = df.to_string()
    else:
        file_content = uploaded_file.read().decode("utf-8")
        st.text(file_content[:500])

# =========================
# 💬 CHAT
# =========================
user_input = st.text_input("Ask something...")

if st.button("Submit"):
    if user_input:

        prompt = f"""
        Question: {user_input}
        Data: {file_content}
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Helpful AI assistant"},
                    {"role": "user", "content": prompt}
                ]
            )

            st.success("✅ Answer:")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.caption("Made by Ravi 🚀")
