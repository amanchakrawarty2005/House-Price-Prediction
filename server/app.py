import streamlit as st
import pandas as pd
import json
import pickle
import os

# -------------------- Page config --------------------
st.set_page_config(
    page_title="Real Estate Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# -------------------- Paths --------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model", "RidgeModel.pkl")
COLUMNS_PATH = os.path.join(BASE_DIR, "model", "columns.json")

# -------------------- Load model --------------------
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# -------------------- Load columns --------------------
with open(COLUMNS_PATH, "r") as f:
    data_columns = json.load(f)["data_columns"]

locations = sorted(data_columns[3:])  # skip sqft, bath, bhk

# -------------------- UI --------------------
st.title("🏠 Real Estate Price Prediction")

st.markdown("Enter the property details to estimate the price.")

location = st.selectbox("Location", locations)
sqft = st.number_input("Total Sqft", min_value=300, max_value=10000, step=50)
bhk = st.number_input("BHK", min_value=1, max_value=10, step=1)
bath = st.number_input("Bathrooms", min_value=1, max_value=10, step=1)

# -------------------- Validation --------------------
def is_valid_bhk(sqft, bhk):
    return bhk <= sqft / 300   # realistic constraint

# -------------------- Prediction --------------------
if st.button("Predict Price"):
    if not is_valid_bhk(sqft, bhk):
        st.error("❌ BHK too high for the given sqft")
    else:
        try:
            input_df = pd.DataFrame([{
                "total_sqft": sqft,
                "bath": bath,
                "bhk": bhk,
                "location": location
            }])

            price = round(float(model.predict(input_df)[0]), 2)

            st.success(f"💰 Estimated Price: ₹ {price} Lakhs")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# -------------------- Footer --------------------
st.markdown("---")
st.caption("Built with Streamlit • ML Pipeline Model")