import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

df = pd.read_csv("data/acne_data.csv")

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(
    y_test,
    predictions
)

print("Mean Absolute Error:")
print(mae)

print("\nFeature Importance:")

for feature, importance in zip(
    X.columns,
    model.feature_importances_
):
    print(
        feature,
        round(importance, 3)
    )