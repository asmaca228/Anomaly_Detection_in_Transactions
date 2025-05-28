#  Anomaly Detection in Transactions
- This project implements a machine learning solution to detect unusual or suspicious financial transactions, helping identify potential fraud or irregularities in transactional data.

## Description
- Anomaly detection is critical in financial systems to flag transactions that deviate from expected behavior. This project leverages the Isolation Forest algorithm, an unsupervised learning method that isolates anomalies effectively, especially in high-dimensional datasets. The solution includes data preprocessing, feature engineering, hyperparameter tuning, and real-time visualization for easy interpretation.

## Key Features

- Data cleaning and exploratory analysis of transactions

- Feature engineering for better model performance

- Anomaly detection using the Isolation Forest algorithm

- Visualizations to understand data distribution and model output

- Hyperparameter tuning for improved accuracy
  
- Real-time visualization with Streamlit

## Model Training 

The anomaly detection model is built using the **Isolation Forest** algorithm, an unsupervised learning technique designed to isolate anomalies efficiently in high-dimensional datasets. The training workflow includes:

1. Data preprocessing (handling missing values, feature engineering)
2. Splitting data into training and testing sets
3. Training the Isolation Forest model with hyperparameter tuning
4. Evaluating model performance 
5. Saving the trained model using `pickle` 

## Techniques & Tools Used

- Python : Core programming language

- Pandas, NumPy : Data manipulation

- Matplotlib, Seaborn : Data visualization

- Scikit-learn : Machine learning (Isolation Forest)
  
- Streamlit : Interactive user interface

- Jupyter Notebook : Development environment

## Installation and Usage
### Prerequisites
- Python
- Git
- Basic knowledge of command line
### Steps
#### 1. Clone the repository:
`git clone https://github.com/asmaca228/Anomaly_Detection_in_Transactions.git`
#### 2. Create and activate a virtual environment (recommended):
- `python -m venv venv`
- `source venv/bin/activate` for Mac and `venv\Scripts\activate` for Windows
#### 3. Install dependencies:
`pip install -r requirements.txt`
#### 4. Launch the Streamlit app for real-time anomaly detection visualization:
`streamlit run app.py`

