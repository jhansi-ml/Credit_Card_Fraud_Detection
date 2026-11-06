import mlflow
import mlflow.sklearn

# Step 1: Connect to MLflow server
mlflow.set_tracking_uri("http://127.0.0.1:5000")

# Step 2: Load registered model
model = mlflow.sklearn.load_model(
    "models:/FraudDetection@champion"
)

print("Registered model loaded successfully!")

# Save the registered model locally
mlflow.sklearn.save_model(
    model,
    path="models/fraud_model",
    serialization_format="cloudpickle"
)

print("Model saved successfully!")

# Load the locally saved model
loaded_model = mlflow.sklearn.load_model("models/fraud_model")

print("Local model loaded successfully!")

print(loaded_model)