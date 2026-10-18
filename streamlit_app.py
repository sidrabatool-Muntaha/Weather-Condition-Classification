
import streamlit as st
import math

st.title("Weather Condition Classification")
st.write("### Machine Learning Model Testing Interface")

st.sidebar.title("About")
st.sidebar.write(
    "This app predicts a weather category using "
    "temperature, humidity, wind speed and cloud cover."
)

st.write("### Enter weather details:")

temperature = st.number_input(
    "Temperature (C)", min_value=-10.0, max_value=50.0, value=25.0
)

humidity = st.number_input(
    "Humidity (%)", min_value=0.0, max_value=100.0, value=40.0
)

wind_speed = st.number_input(
    "Wind Speed (km/h)", min_value=0.0, max_value=150.0, value=10.0
)

cloud_cover = st.number_input(
    "Cloud Cover (%)", min_value=0.0, max_value=100.0, value=10.0
)

# Sample training data:
# temperature, humidity, wind, cloud cover, weather
data = [
    [30, 30, 5, 10, "Sunny"],
    [28, 40, 10, 20, "Sunny"],
    [32, 35, 8, 5, "Sunny"],
    [25, 45, 12, 15, "Sunny"],
    [20, 60, 10, 50, "Cloudy"],
    [18, 65, 15, 70, "Cloudy"],
    [22, 55, 8, 60, "Cloudy"],
    [15, 70, 12, 80, "Cloudy"],
    [18, 90, 20, 95, "Rainy"],
    [22, 85, 25, 90, "Rainy"],
    [16, 95, 15, 100, "Rainy"],
    [20, 88, 18, 85, "Rainy"]
]

if st.button("Test Model"):

    test_data = [
        temperature, humidity, wind_speed, cloud_cover
    ]

    distances = []

    # Compare input with every training example
    for row in data:
        distance = math.sqrt(
            ((test_data[0] - row[0]) / 60) ** 2 +
            ((test_data[1] - row[1]) / 100) ** 2 +
            ((test_data[2] - row[2]) / 150) ** 2 +
            ((test_data[3] - row[3]) / 100) ** 2
        )

        distances.append((distance, row[4]))

    # Find the closest example
    distances.sort(key=lambda item: item[0])
    prediction = distances[0][1]

    st.subheader("Prediction Result")

    if prediction == "Sunny":
        st.success("Predicted Weather: SUNNY")
    elif prediction == "Cloudy":
        st.info("Predicted Weather: CLOUDY")
    else:
        st.warning("Predicted Weather: RAINY")

    st.write("Prediction based on the closest training example.")
