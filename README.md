# Credit Card Fraud Detection | End-to-End Machine Learning Project

## Project Overview

An end-to-end Machine Learning application that identifies potentially fraudulent credit card transactions using a Random Forest Classifier.

This project demonstrates the complete ML lifecycle, including exploratory data analysis, data preprocessing, model training, evaluation, MLflow model management, FastAPI development, Docker containerization, and cloud deployment on Render.

## Live Application

- **Live API:** [https://credit-card-fraud-detection-opsh.onrender.com/]
- **Interactive API Documentation:** [https://credit-card-fraud-detection-opsh.onrender.com/docs]
- **GitHub Repository:** https://github.com/jhansi-ml/Credit_Card_Fraud_Detection

## Business Problem

Credit card fraud causes financial losses for customers and financial institutions. Detecting suspicious transactions accurately is important for reducing fraud-related losses.

The objective of this project is to build a classification model that identifies fraudulent transactions while balancing fraud detection (recall) and false alarms (precision).

## Dataset

- Dataset: Credit Card Fraud Detection
- Working dataset: 10,000 transaction records
- Target variable: `Class`
  - `0` – Legitimate transaction
  - `1` – Fraudulent transaction
- Features: `Time`, `Amount`, and anonymized features `V1` to `V28`
- The dataset is highly imbalanced, with legitimate transactions significantly outnumbering fraudulent transactions.

## Machine Learning Workflow

1. **Exploratory Data Analysis (EDA)**
   - Examined dataset structure and distributions.
   - Checked missing values and duplicate records.
   - Analyzed class imbalance.
   - Visualized transaction amounts and outliers.

2. **Data Preprocessing**
   - Prepared training and testing datasets.
   - Applied StandardScaler.
   - Addressed class imbalance using class weights.

3. **Model Development**
   - Trained and compared classification algorithms.
   - Experimented with Logistic Regression and Random Forest.
   - Selected a Random Forest model for the deployed API.

4. **Model Evaluation**
   - Evaluated classification performance using precision, recall, F1-score, and confusion matrix.
   - Focused on fraud-class detection rather than accuracy alone.

5. **MLflow Model Management**
   - Tracked model experiments.
   - Registered the selected model.
   - Saved the model artifact for API inference.

6. **Deployment**
   - Developed a REST API using FastAPI.
   - Containerized the application using Docker.
   - Deployed the API on Render.

## Model Details

- Algorithm: Random Forest Classifier
- Preprocessing: StandardScaler
- Imbalance handling: `class_weight="balanced"`
- Model artifact: MLflow model format
- Prediction type: Binary classification

The preprocessing and classification steps are saved together as a pipeline to ensure consistent transformations during inference.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Experiment Tracking | MLflow |
| API Development | FastAPI, Pydantic |
| Database | SQLite |
| Containerization | Docker |
| Cloud Deployment | Render |
| Version Control | Git, GitHub |

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API health |
| GET | `/sample/{transaction_type}` | Retrieve a sample transaction |
| POST | `/predict` | Predict whether a transaction is fraudulent |
| GET | `/predictions` | Retrieve logged predictions |

### API Documentation

Visit `/docs` on the deployed application to explore and test the endpoints using Swagger UI.

### Example Prediction Response

```json
{
  "prediction": 1,
  "result": "Fraud",
  "fraud_probability": 0.92,
  "message": "Potential fraudulent transaction detected"
}
```

*Example response only; actual probability and message depend on the model output.*

## Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/jhansi-ml/Credit_Card_Fraud_Detection.git
cd Credit_Card_Fraud_Detection
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI application

```bash
uvicorn app.main:app --reload
```

### 5. Open API documentation

```text
http://127.0.0.1:8000/docs
```

## Run Using Docker

### Build the Docker image

```bash
docker build -t fraud-detection-api .
```

### Run the container

```bash
docker run -d -p 8000:8000 --name fraud-detection-container fraud-detection-api
```

### Access the application

```text
http://localhost:8000/docs
```

## Project Structure

```text
Credit_Card_Fraud_Detection/
│
├── app/
│   └── main.py
│
├── data/
│   ├── creditcard10000.csv
│   └── test_transactions.py
│
├── models/
│   └── fraud_model/
│       ├── MLmodel
│       ├── model.pkl
│       ├── conda.yaml
│       ├── python_env.yaml
│       └── requirements.txt
│
├── Notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_train_test_split.ipynb
│   └── 03_preprocessing_model_training_evaluation.ipynb
│
├── screenshots/
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
└── README.md
```

## Key Learning Outcomes

- Built an end-to-end machine learning classification pipeline.
- Worked with imbalanced classification data.
- Compared multiple ML algorithms.
- Used MLflow for experiment tracking and model management.
- Developed REST APIs using FastAPI.
- Integrated SQLite for prediction logging.
- Containerized an ML application using Docker.
- Deployed a machine learning API on Render.

## Future Improvements

- Add model performance monitoring.
- Evaluate prediction drift.
- Experiment with advanced imbalanced-learning techniques.
- Improve model performance using additional data.
- Integrate persistent database storage for production use.

---

**Author:** Jhansi Konamoni

**GitHub:** https://github.com/jhansi-ml

**LinkedIn:** https://www.linkedin.com/in/jhansi-konamoni
