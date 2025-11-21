import streamlit as st
import pandas as pd
import pickle

# -------------------------
# Load the trained model
# -------------------------
model_path = "crop_selection_model_RF.pkl"   # change if different
with open(model_path, "rb") as f:
    model = pickle.load(f)

st.title("🌾 SeedAI – Crop Selection Recommendation System")
st.write("Provide your soil and climate details to get the best crop suggestion.")

# -------------------------
# Crop images (Add all crop images here later)
# -------------------------
crop_images = {
    "Groundnut": "images/groundnut.jpeg",
    "Rice": "images/rice.jpeg",
    "Maize": "images/maize.jpeg",
    "Cotton": "images/cotton.jpeg",
    "Banana": "images/banana.jpeg",
    "Turmeric": "images/turmeric.jpeg",
    "Onion": "images/onion.jpeg",
    "Tomato": "images/tomato.jpeg",
    "Sesame": "images/sesame.jpeg",
    "Sugarcane":"images/sugarcane.jpeg",
    "Wheat":"images/wheat.jpeg",
    "Barley":"images/barley.jpeg",
    "Mustard":"images/mustard.jpeg"
}

# -------------------------
# Crop descriptions
# -------------------------
crop_info = {
    
    "Groundnut": "Groundnut – Grows well in sandy loam soil with moderate rainfall.",
    "Rice": "Rice – Best suited for high-water clayey or loamy soils.",
    "Maize": "Maize – Thrives in well-drained fertile soils with warm climate.",
    "Cotton": "Cotton – Prefers black soil and hot, dry weather.",
    "Banana": "Banana – Requires high moisture, warm climate, and fertile soil.",
    "Turmeric": "Turmeric – Grows well in loose, loamy soil rich in organic matter.",
    "Onion": "Onion – Best grown in sandy loam soils with good drainage.",
    "Tomato": "Tomato – Prefers warm climates and well-drained soils.",
    "Sesame": "Sesame – Drought-tolerant crop suited for light, dry soils.",
    "Sugarcane": "Sugarcane – Requires high rainfall and fertile, deep soils.",
    "Wheat": "Wheat – Grows well in well-drained loamy soils with cool climate.",
    "Barley": "Barley – Tolerates dry climates and grows in medium fertility soils.",
    "Mustard": "Mustard – Prefers cool weather and sandy to loamy soil."
}


# -------------------------
# User Inputs
# -------------------------
season = st.selectbox("Season", ["Kharif", "Rabi", "Summer"])

pH = st.number_input("Soil pH", 0.0, 14.0, 7.0)
nitrogen = st.number_input("Nitrogen (kg/ha)", 0.0, 500.0, 250.0)
clay = st.number_input("Clay (%)", 0.0, 100.0, 35.0)
sand = st.number_input("Sand (%)", 0.0, 100.0, 35.0)
silt = st.number_input("Silt (%)", 0.0, 100.0, 30.0)
soc = st.number_input("SOC (mg/kg)", 0.0, 500.0, 200.0)
bdod = st.number_input("BDOD", 0.0, 500.0, 130.0)
cec = st.number_input("CEC", 0.0, 1000.0, 280.0)

rainfall = st.number_input("Rainfall (mm)", 0.0, 5000.0, 1500.0)
temperature = st.number_input("Temperature (°C)", 0.0, 60.0, 28.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 75.0)
solar = st.number_input("Solar Radiation (W/m²)", 0.0, 2000.0, 250.0)

# -------------------------
# Prepare input for prediction
# -------------------------
input_df = pd.DataFrame({
    "Season": [season],
    "pH": [pH],
    "Nitrogen": [nitrogen],
    "Clay": [clay],
    "Sand": [sand],
    "Silt": [silt],
    "SOC": [soc],
    "BDOD": [bdod],
    "CEC": [cec],
    "Rainfall": [rainfall],
    "Temperature": [temperature],
    "Humidity": [humidity],
    "Solar": [solar]
})

# -------------------------
# Predict Button
# -------------------------
if st.button("Recommend Crop"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"🌱 **Recommended Crop: {prediction}**")

        # Show image
        if prediction in crop_images:
            st.image(crop_images[prediction], caption=prediction, use_column_width=True)
        else:
            st.warning("No image available for this crop.")

        # Show description
        if prediction in crop_info:
            st.info(crop_info[prediction])
        else:
            st.text("Crop information not available.")

    except Exception as e:
        st.error(f"Prediction error: {e}")
