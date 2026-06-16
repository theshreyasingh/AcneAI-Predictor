import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("data/acne_data.csv")

# Convert Yes/No to numbers
df["Oily_Food"] = df["Oily_Food"].map({
    "No": 0,
    "Yes": 1
})

X = df[
    [
        "Sleep_Hours",
        "Water_Liters",
        "Stress_Level",
        "Oily_Food"
    ]
]

y = df["Acne_Severity"]

model = RandomForestRegressor()

model.fit(X, y)

prediction = model.predict(
    [[5, 1.5, 5, 1]]
)

print("Predicted Acne Severity:")
print(prediction)