import streamlit as st
import joblib
import numpy as np

@st.cache_resource
def load_model():
    return joblib.load("xgboost_car_price_model.pkl")

model = load_model()

st.set_page_config(page_title="Car Price Predictor", layout="centered")
st.title(" Car Selling Price Predictor")
st.markdown("---")

with st.form("input_form"):
    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Car Name", placeholder="e.g., Maruti Swift")
        year = st.number_input("Manufacturing Year", min_value=1990, max_value=2025, value=2020)
        km_driven = st.number_input("Kilometers Driven", min_value=0, value=50000, step=1000)

        fuel_options = ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
        fuel = st.selectbox("Fuel Type", options=fuel_options)

        seller_options = ["Dealer", "Individual", "Trustmark Dealer"]
        seller_type = st.selectbox("Seller Type", options=seller_options)

        transmission_options = ["Automatic", "Manual"]
        transmission = st.selectbox("Transmission", options=transmission_options)

        owner_options = [
            "First Owner", "Second Owner", "Third Owner", 
            "Fourth & Above Owner", "Test Drive Car"
        ]
        owner = st.selectbox("Owner Type", options=owner_options)

        Mileage = st.number_input("Mileage (kmpl)", min_value=0.0)
        engine = st.number_input("Engine (CC)", min_value=0)

    with col2:
        max_power = st.number_input("Max Power (bhp)", min_value=0.0)
        Seats = st.number_input("Seat", min_value=0)

        brand_options = [
            "Maruti", "Skoda", "Honda", "Hyundai", "Toyota", "Ford", "Renault", "Mahindra",
            "Tata", "Chevrolet", "Fiat", "Datsun", "Jeep", "Mercedes-Benz", "Mitsubishi", "Audi",
            "Volkswagen", "BMW", "Nissan", "Lexus", "Jaguar", "Land", "MG", "Volvo", "Daewoo",
            "Kia", "Force", "Ambassador", "Ashok", "Isuzu", "Opel", "Peugeot"
        ]
        brand = st.selectbox("Brand", options=brand_options)

        is_popular = st.checkbox("Popular Model")
        is_luxury = st.checkbox("Luxury Car")
        high_mileage = st.checkbox("High Mileage")

    submit = st.form_submit_button("Predict Selling Price", use_container_width=True)

if submit:
    try:
        age = 2025 - year

        if age <= 3:
            age_category_code = 1  # recent
            age_category = "Recent"
        elif age <= 10:
            age_category_code = 0  # old
            age_category = "Old"
        else:
            age_category_code = 2  # very old
            age_category = "Very Old"

        if fuel.lower() == "diesel":
            if Mileage >= 20:
                fuel_efficiency_code = 1
            elif Mileage >= 15:
                fuel_efficiency_code = 0
            else:
                fuel_efficiency_code = 2
        elif fuel.lower() == "petrol":
            if Mileage >= 17:
                fuel_efficiency_code = 1
            elif Mileage >= 13:
                fuel_efficiency_code = 0
            else:
                fuel_efficiency_code = 2
        else:  # CNG, LPG, Electric
            if Mileage >= 20:
                fuel_efficiency_code = 1
            elif Mileage >= 15:
                fuel_efficiency_code = 0
            else:
                fuel_efficiency_code = 2

        fuel_mapping = {"Petrol": 4, "Diesel": 1, "CNG": 0, "LPG": 3, "Electric": 2}
        seller_mapping = {"Dealer": 0, "Individual": 1, "Trustmark Dealer": 2}
        transmission_mapping = {"Manual": 1, "Automatic": 0}
        owner_mapping = {
            "First Owner": 0,
            "Second Owner": 2,
            "Third Owner": 4,
            "Fourth & Above Owner": 1,
            "Test Drive Car": 3,
        }
        brand_mapping = {
            "Maruti": 20, "Skoda": 27, "Honda": 10, "Hyundai": 11, "Toyota": 29, "Ford": 9,
            "Renault": 26, "Mahindra": 19, "Tata": 28, "Chevrolet": 4, "Fiat": 7, "Datsun": 6,
            "Jeep": 14, "Mercedes-Benz": 21, "Mitsubishi": 22, "Audi": 2, "Volkswagen": 30,
            "BMW": 3, "Nissan": 23, "Lexus": 17, "Jaguar": 13, "Land": 16, "MG": 18, "Volvo": 31,
            "Daewoo": 5, "Kia": 15, "Force": 8, "Ambassador": 0, "Ashok": 1, "Isuzu": 12,
            "Opel": 24, "Peugeot": 25
        }

        input_data = np.array([[
            year,
            km_driven,
            fuel_mapping[fuel],
            seller_mapping[seller_type],
            transmission_mapping[transmission],
            owner_mapping[owner],
            Mileage,
            engine,
            max_power,
            Seats,
            age,
            brand_mapping[brand],
            int(is_popular),
            int(is_luxury),
            int(high_mileage),
            age_category_code,
            fuel_efficiency_code
        ]])

        prediction = model.predict(input_data)[0]

        st.success(f"Estimated Selling Price: {int(prediction):,}")

        # Confidence
        confidence = "High"
        if age > 15 or km_driven > 200000:
            confidence = "Medium"
        if age > 20 or km_driven > 300000:
            confidence = "Low"
        st.info(f"**Prediction Confidence:** {confidence}")

        # Input summary
        with st.expander("Input Summary"):
            col1, col2 = st.columns(2)
            with col1:
                st.write(f"**Car:** {name}")
                st.write(f"**Brand:** {brand}")
                st.write(f"**Year:** {year}")
                st.write(f"**Age:** {age} years ({age_category})")
                st.write(f"**Kilometers Driven:** {km_driven:,}")
                st.write(f"**Fuel:** {fuel}")
            with col2:
                st.write(f"**Seller Type:** {seller_type}")
                st.write(f"**Transmission:** {transmission}")
                st.write(f"**Owner:** {owner}")
                st.write(f"**Popular Model:** {'Yes' if is_popular else 'No'}")
                st.write(f"**Luxury Car:** {'Yes' if is_luxury else 'No'}")
                st.write(f"**High Mileage:** {'Yes' if high_mileage else 'No'}")

        st.markdown("---")
        lower = int(prediction * 0.85)
        upper = int(prediction * 1.15)
        st.write(f"** Price Range Estimation:**{lower:,} – {upper:,}")

    except Exception as e:
        st.error(f" Error: {str(e)}")
        st.info("Please check that all required fields are filled properly.")

st.markdown("---")
st.markdown(
    "*Disclaimer: This prediction is based on historical data and may not reflect actual market prices.*"
)
