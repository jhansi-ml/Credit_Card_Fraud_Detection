import mlflow
import mlflow.sklearn
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel, Field
import pandas as pd
from pathlib import Path
import sqlite3
import json
from datetime import datetime, timezone

BASE_DIR = Path(__file__).resolve().parent.parent

# Load locally saved registered model
MODEL_PATH = BASE_DIR / "models" / "fraud_model"

model = mlflow.sklearn.load_model(str(MODEL_PATH))

print("Fraud Detection model loaded successfully!")

DATA_PATH = BASE_DIR / "data" / "creditcard10000.csv"

df = pd.read_csv(DATA_PATH)

app = FastAPI(
    title="Credit Card Fraud Detection API",
    description="API to detect fraudulent credit card transactions",
    version="1.0"
)

# Define path to SQLite database
DB_PATH = BASE_DIR / "predictionsDB.db"

#create a connection to the SQLite database
def create_database():
    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            prediction INTEGER,
            result TEXT,
            fraud_probability REAL,
            transaction_data TEXT   
        )
    ''')  
    conn.commit()
    conn.close()
create_database()
    
      
# Define input features
class Transaction(BaseModel):
    Time: float=Field(ge=0)

    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float=Field(ge=0)
    
   

@app.get("/")
def home():
    return {
        "message": "Credit Card Fraud Detection API is running"
    }

@app.get("/sample/{transaction_type}")
def get_sample_transaction(transaction_type: str):

    if transaction_type == "legitimate":
        sample = df[df["Class"] == 0].iloc[0]

    elif transaction_type == "fraudulent":
        sample = df[df["Class"] == 1].iloc[0]

    else:
        raise HTTPException(
            status_code=400,
            detail="Choose legitimate or fraudulent"
        )

    features = sample.drop("Class").to_dict()

    return {
        key: float(value)
        for key, value in features.items()
    }
    
@app.post("/predict")
def predict_transaction(transaction: Transaction):

    # Convert input into DataFrame
    input_data = pd.DataFrame(
        [transaction.model_dump()]
    )

    # Predict class
    prediction = model.predict(input_data)[0]

    # Predict fraud probability
    probability = model.predict_proba(input_data)[0][1]

    # Convert prediction into readable output
    result = (
        "Fraudulent Transaction"
        if prediction == 1
        else "Legitimate Transaction"
    )
    timestamp = datetime.now(timezone.utc).isoformat()

    transaction_json = json.dumps(transaction.model_dump())

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO predictions (
            timestamp,
            prediction,
            result,
            fraud_probability,
            transaction_data
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        timestamp,
        int(prediction),
        result,
        float(probability),
        transaction_json
    ))

    conn.commit()
    conn.close()


    return {
        "prediction": int(prediction),
        "result": result,
        "fraud_probability": round(float(probability), 4),
        "message": "Prediction stored in the database successfully"
    }
    
@app.get("/predictions")
def get_predictions():

    conn = sqlite3.connect(DB_PATH)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            timestamp,
            prediction,
            result,
            fraud_probability
        FROM predictions
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    predictions = [dict(row) for row in rows]

    conn.close()

    return {
        "total_predictions": len(predictions),
        "predictions": predictions
    }
