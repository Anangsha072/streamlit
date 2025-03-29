# streamlit
# AI-Powered Travel Planner Documentation

## **Introduction**

The AI-Powered Travel Planner is a Streamlit-based web application that helps users generate personalized travel itineraries based on their preferences, budget, and destination. It leverages Google Gemini AI to curate travel plans with real-time data.

---

## **Features**

- Collects user inputs like **destination, budget, duration, and preferences**.
- Uses **Google Gemini AI** to generate personalized itineraries.
- Suggests **top attractions, hidden gems, food recommendations, and travel tips**.
- Provides an interactive and user-friendly **Streamlit** interface.
- Hosted on **Streamlit Cloud** for easy access.

---

## **Installation**

### **1. Clone the Repository**

```sh
git clone https://github.com/yourusername/ai-travel-planner.git
cd ai-travel-planner
```

### **2. Create a Virtual Environment (Optional but Recommended)**

```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
```

### **3. Install Dependencies**

```sh
pip install -r requirements.txt
```

### **4. Set Up Environment Variables**

## **Usage**

### **Run the Application**


streamlit run app.py


Once the server starts, open the **Local URL** (e.g., `http://localhost:8501`) in your browser.

---

## **Code Structure**

```
/travel-planner
  ├── app.py                 # Main Streamlit application
  ├── requirements.txt        # Dependencies
  ├── .env                    # API key (Not pushed to GitHub)
  ├── README.md               # Project Documentation
```

---

## **Deployment**

### **1. Push to GitHub**

```sh
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

### **2. Deploy on Streamlit Cloud**

1. Go to [Streamlit Community Cloud](https://share.streamlit.io/)
2. Click **“New App”** → Select your GitHub repository.
3. Configure:
   - **Main file path**: `app.py`
   - **Dependencies**: It will auto-detect `requirements.txt`
4. Click **“Deploy”** 🚀

### **3. Get Your Public URL**

Once deployed, Streamlit Cloud provides a **public URL** to share with users.

---

## **API Integration**

The application integrates with **Google Gemini AI** to generate itineraries. The `generate_itinerary` function sends a prompt to the API and retrieves travel recommendations.

### **API Request Structure**

```python
import google.generativeai as genai

def generate_itinerary(destination, budget, trip_duration, preferences):
    prompt = f"""
    Generate a {trip_duration}-day itinerary for {destination}.
    - Budget: {budget}
    - Preferences: {preferences}
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text.strip()
```

### **Handling API Errors**

If there’s an issue with the API, the application displays a relevant error message, such as **invalid API key** or **quota exceeded**.

---

## **Future Enhancements**

- **Multi-language support** for global travelers.
- **Integration with live travel APIs** (Google Places, TripAdvisor, etc.).
- **User accounts** to save favorite itineraries.
- **Flight & hotel recommendations** based on budget.

---

## **Contributing**

If you’d like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit (`git commit -m "Added new feature"`).
4. Push the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## **License**

This project is open-source and available under the **MIT License**.

---

## **Contact**

For any questions or feedback, contact: 📧 Email: anangshadas1@gmail.com
🔗 GitHub: https://github.com/Anangsha072 


to view the app click on https://app-gdnczybh8mdqkxhs5edhyh.streamlit.app/
