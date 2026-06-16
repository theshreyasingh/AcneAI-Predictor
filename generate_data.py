import pandas as pd
import random

data = []

for day in range(1, 201):

    sleep = random.randint(4, 9)
    water = round(random.uniform(1, 4), 1)
    stress = random.randint(1, 5)
    oily_food = random.choice(["Yes", "No"])

    acne = 1

    if sleep < 6:
        acne += 1

    if water < 2:
        acne += 1

    if stress >= 4:
        acne += 1

    if oily_food == "Yes":
        acne += 1

    acne = min(acne, 5)

    data.append([
        sleep,
        water,
        stress,
        oily_food,
        acne
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Sleep_Hours",
        "Water_Liters",
        "Stress_Level",
        "Oily_Food",
        "Acne_Severity"
    ]
)

df.to_csv("data/acne_data.csv", index=False)

print("Dataset created successfully!")
print(df.head())