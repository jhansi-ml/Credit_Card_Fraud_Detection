# Load the locally saved model
import mlflow
import mlflow.sklearn

loaded_model = mlflow.sklearn.load_model("models/fraud_model")

print("Local model loaded successfully!")

print(loaded_model)