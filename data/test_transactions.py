
import pandas as pd

# Load your dataset
df = pd.read_csv("data/creditcard10000.csv")

# Get one legitimate transaction
legitimate = df[df["Class"] == 0].iloc[[0]]

# Get one fraudulent transaction
fraudulent = df[df["Class"] == 1].iloc[[0]]

# Remove target column
legitimate_input = legitimate.drop(columns=["Class"])
fraudulent_input = fraudulent.drop(columns=["Class"])

# Display JSON data for Swagger
print("\nLEGITIMATE TRANSACTION:")
print(legitimate_input.to_json(orient="records", indent=4))

print("\nFRAUDULENT TRANSACTION:")
print(fraudulent_input.to_json(orient="records", indent=4))
