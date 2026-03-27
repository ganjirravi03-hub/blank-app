import streamlit as st
import pandas as pd
import openai

# 🔑 API Key (yaha apni key daal)
openai.api_key = "YOUR_OPENAI_API_KEY"

st.set_page_config(page_title="AI Assistant", layout="centered")

st.title("🤖 AI Smart Assistant")
st.write("Chat + File Analysis System 🚀")

# =========================
# 📂 FILE UPLOAD SECTION
# =========================
uploaded_file = st.file_uploader("Upload your file (CSV or TXT)", type=["csv", "txt"])

file_content = ""

if uploaded_file is not None:
    if uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        st.write("📊 CSV Preview:")
        st.dataframe(df.head())
        file_content = df.to_string()
    else:
        file_content = uploaded_file.read().decode("utf-8")
        st.write("📄 File Content Preview:")
        st.text(file_content[:500])

# =========================
# 💬 CHAT SECTION
# =========================
user_input = st.text_input("Ask something...")

if st.button("Submit"):
    if user_input:

        prompt = f"""
        User Question: {user_input}
        
        File Data:
        {file_content}
        """

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            answer = response['choices'][0]['message']['content']

            st.success("✅ Response:")
            st.write(answer)

        except Exception as e:
            st.error(f"Error: {e}")

# =========================
# 🧠 FOOTER
# =========================
st.markdown("---")
st.caption("Made with ❤️ by Ravi AI System")
