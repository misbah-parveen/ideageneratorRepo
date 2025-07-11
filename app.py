import streamlit as st
import google.generativeai as genai

# 🔐 Replace with your actual API Key from Google AI Studio
GOOGLE_API_KEY = "AIzaSyD5-QAal0"

# Configure Gemini API
genai.configure(api_key="AIzaSyCPiKT6AL8OQqd8OdLZu6O5q7LA43ONK-o")
model = genai.GenerativeModel("gemini-2.0-flash-exp")

# Streamlit App GUI
st.set_page_config(page_title="Startup Idea Generator", page_icon="")
st.title(" AI Startup Idea Generator")
st.markdown("**Generate 5 unique startup ideas in your chosen industry and language.**")

# User Inputs
industry = st.text_input("Enter an Industry (e.g., Fashion, Health, Education)", "")
language = st.selectbox("Select Language", ["English", "Urdu", "Spanish", "German"])
generate_button = st.button(" SEND")
st.markdown('<style>body, .stApp {background-color: black; color: white;}</style>', unsafe_allow_html=True)


# Generate Response
if generate_button:
    if industry.strip() == "":
        st.warning("⚠️ Please enter an industry.")
    else:
        with st.spinner("Generating ideas..."):
            prompt = f"""
Act like a business expert. Generate 5 unique startup ideas in the "{industry}" industry.
For each idea, include:
1. Idea Name
2. The Problem it Solves
3. The Solution
4. Target Users
5. Why the Idea is Innovative

Write the response in {language} language.
"""
            try:
                response = model.generate_content(prompt)
                st.success(f"✅ 5 Startup Ideas in {industry} ({language})")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"❌ Error generating ideas: {e}")
