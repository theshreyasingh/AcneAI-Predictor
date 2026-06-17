import plotly.express as px
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load data
df = pd.read_csv("data/acne_data.csv")

# Convert Yes/No to 0/1
df["Oily_Food"] = df["Oily_Food"].map({
    "No": 0,
    "Yes": 1
})

# Features and target
X = df[
    [
        "Sleep_Hours",
        "Water_Liters",
        "Stress_Level",
        "Oily_Food"
    ]
]

y = df["Acne_Severity"]

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X, y)

# UI
st.title("🤖 AcneAI – Lifestyle-Based Acne Risk Prediction System")

st.write(
    "This AI model predicts acne severity using lifestyle factors such as sleep, hydration, stress levels, and dietary habits."
)

sleep = st.slider(
    "Sleep Hours",
    4,
    10,
    7
)

water = st.slider(
    "Water Intake (Liters)",
    1.0,
    5.0,
    2.5
)

stress = st.slider(
    "Stress Level",
    1,
    5,
    3
)

oily_food = st.selectbox(
    "Oily Food Consumed?",
    ["No", "Yes"]
)
if st.button("Predict Acne Severity"):

    oily = 1 if oily_food == "Yes" else 0

    input_data = pd.DataFrame({
        "Sleep_Hours": [sleep],
        "Water_Liters": [water],
        "Stress_Level": [stress],
        "Oily_Food": [oily]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Acne Severity: {prediction[0]:.2f}/5"
    )

    if stress >= 4:
        st.warning(
            "⚠️ High stress levels may contribute to acne flare-ups."
        )

    if water < 2:
        st.info(
            "💧 Your water intake appears low. Staying hydrated may help support healthy skin."
        )

    if sleep < 6:
        st.warning(
            "😴 Low sleep duration may negatively affect skin recovery."
        )

    if oily_food == "Yes":
        st.info(
            "🍔 Frequent oily food consumption may be associated with increased acne severity."
        )

        st.subheader("Factors Influencing Acne Severity")

st.write("Stress Level : 35.9%")
st.write("Oily Food : 24.9%")
st.write("Water Intake : 22.7%")
st.write("Sleep Hours : 16.5%")

st.markdown("---")
st.header("📝 Daily Acne Log")

actual_acne = st.slider(
    "Today's Actual Acne Severity",
    1,
    5,
    2
)

if st.button("Save Today's Entry"):

    from datetime import date

    new_entry = pd.DataFrame({
        "Date": [str(date.today())],
        "Sleep_Hours": [sleep],
        "Water_Liters": [water],
        "Stress_Level": [stress],
        "Oily_Food": [oily_food],
        "Acne_Severity": [actual_acne]
    })

    tracker_file = "data/acne_tracker.csv"

    try:
        old_data = pd.read_csv(tracker_file)
        updated_data = pd.concat(
            [old_data, new_entry],
            ignore_index=True
        )
    except FileNotFoundError:
        updated_data = new_entry

    updated_data.to_csv(
        tracker_file,
        index=False
    )

    st.success(
        "✅ Daily entry saved successfully!"
    )
st.markdown("---")
st.header("📊 Acne Progress Dashboard")

try:
    tracker_df = pd.read_csv(
        "data/acne_tracker.csv"
    )

    st.write(tracker_df)

    fig = px.line(
        tracker_df,
        x="Date",
        y="Acne_Severity",
        title="Acne Severity Over Time"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

except:
    st.info(
        "Add more entries to see dashboard analytics."
    )