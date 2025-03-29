import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get Google Gemini API Key
GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")

# Validate API Key
if not GEMINI_API_KEY:
    st.error("❌ Google Gemini API key is missing or invalid! Please check your .env file.")
    st.stop()

# Configure Google Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate itinerary using Google Gemini
def generate_itinerary(destination, budget, trip_duration, preferences):
    prompt = f"""
    You are an AI travel assistant. Generate a {trip_duration}-day itinerary for {destination}.
    
    - **Budget**: {budget}
    - **Preferences**: {preferences}
    
    ### Itinerary should include:
    - 🌅 Morning, 🌇 Afternoon, and 🌙 Evening activities.
    - 🏛️ Famous landmarks & hidden gems.
    - 🍽️ Food recommendations.
    - 🚗 Travel tips & local insights.
    """

    try:
        # Use the latest Gemini model
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # 🔥 Updated model name
        response = model.generate_content(prompt)

        # Extract response content properly
        if hasattr(response, "text"):
            return response.text.strip()
        elif hasattr(response, "candidates") and response.candidates:
            return response.candidates[0].content.parts[0].text.strip()
        else:
            return "⚠️ Unexpected response format from Gemini API."

    except Exception as e:
        return f"❌ API Error: {str(e)}"

# Streamlit UI
st.title("✈️ AI Travel Planner (Google Gemini)")

destination = st.text_input("📍 Destination")
budget = st.selectbox("💰 Budget", ["Budget", "Mid-range", "Luxury"])
trip_duration = st.slider("📅 Trip Duration (days)", 1, 14, 5)
preferences = st.text_area("🎯 Preferences (e.g., beaches, history, adventure)")

if st.button("🛫 Generate Itinerary"):
    if not destination:
        st.error("⚠️ Please enter a destination.")
    else:
        with st.spinner("⏳ Generating itinerary..."):
            itinerary = generate_itinerary(destination, budget, trip_duration, preferences)
            st.subheader(f"📌 Your {trip_duration}-Day Itinerary for {destination}")
            st.write(itinerary)





