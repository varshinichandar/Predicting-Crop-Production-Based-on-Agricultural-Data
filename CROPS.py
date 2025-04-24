import streamlit as st
import pandas as pd
import joblib
import os

st.title("🌾 Crop Production Predictor")

# to load model
@st.cache_resource
def load_model(path):
    return joblib.load(path)

# to get model file path
BASE_DIR = os.path.dirname(__file__)
model_path = os.path.join(BASE_DIR, "model.pkl")

# to load the model or stop if missing
try:
    model = load_model(model_path)
except FileNotFoundError:
    st.error("Can't find model.pkl. Please add it here.")
    st.stop()

# to get user inputs
st.write("### Enter crop details:")
item_code = st.number_input("Item Code", min_value=0)
area = st.number_input("Area (ha)", min_value=0.0)
yield_val = st.number_input("Yield (kg/ha)", min_value=0.0)
prod_animals = st.number_input("Animals value", min_value=0.0)
laying = st.number_input("Laying value", min_value=0.0)
carcass = st.number_input("Carcass value", min_value=0.0)
milk = st.number_input("Milk value", min_value=0.0)

# to predict when button clicked
if st.button("Predict"):
    # to prepare input dataframe
    input_df = pd.DataFrame([[
        item_code, area, yield_val,
        prod_animals, laying, carcass, milk
    ]], columns=[
        "Item Code (CPC)",
        "Area_Harvested_in_Hectares",
        "Yield_Value in kg/ha",
        "Producing Animals/Slaughtered_Value",
        "Laying_Value",
        "Yield/Carcass Weight_Value",
        "Milk Animals_Value"
    ])
    # to get prediction
    try:
        pred = model.predict(input_df)[0]
        st.write(f"**Prediction:** {pred:.2f}")
    except:
        st.error("Prediction error.")

# to load and show sample data
st.write("### Data preview")
csv_path = os.path.join(BASE_DIR, "cleansed_crop_data.csv")
try:
    df = pd.read_csv(csv_path)
    st.dataframe(df.head(5))
    # to allow download
    st.download_button("Download data", df.to_csv(index=False), "data.csv")
except FileNotFoundError:
    st.write("Add cleansed_crop_data.csv to see data.")

