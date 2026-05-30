# 🏦 Customer Churn & 💵 Salary Prediction (Deep Learning ANN)

Welcome to the Bank Customer Prediction project! This project contains two Artificial Neural Network (ANN) models:
1. **Classification Model**: Predicts whether a bank customer is likely to leave (churn) or stay.
2. **Regression Model**: Predicts the estimated salary of a customer based on their profile.

🚀 **[Try the Churn Prediction App Here!](https://annproject-5zctv7sjdshcazkdec6aut.streamlit.app/)**
🚀 **[Try the Salary Prediction App Here!](https://annproject-awkjbvappya2uvqmmidpnb.streamlit.app/)**

---

## 📖 Overview
Customer analytics are critical for financial institutions. These deep learning models analyze various customer features—such as Geography, Gender, Age, Credit Score, and Account Balance—to accurately predict customer churn and estimate salaries.

The interactive web interfaces are built using **Streamlit**, providing a user-friendly way to input customer details and instantly receive predictions.

## 🛠️ Technologies Used
- **Deep Learning Framework:** TensorFlow / Keras
- **Web App Framework:** Streamlit
- **Data Manipulation:** Pandas, NumPy
- **Machine Learning Utilities:** Scikit-Learn (StandardScaler, LabelEncoder, OneHotEncoder)
- **Model Tracking:** TensorBoard

## ⚙️ How to Run Locally

If you want to run or modify this project on your own machine, follow these steps:

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <your-repo-url>
   cd "Deep Learing ANN Project"
   ```

2. **Activate your Virtual Environment (Recommended):**
   ```bash
   # On Windows
   .\venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install the Requirements:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit Apps:**
   ```bash
   # Run Churn Prediction App
   streamlit run app.py
   
   # Run Salary Prediction App
   streamlit run streamlit_regression.py
   ```

5. **View the App:**
   Open your browser and navigate to `http://localhost:8501`.

## 📊 Model Training
If you want to see how the models were built and trained, check out the following notebooks:
- `experiments.ipynb`: Contains the workflow for the Churn Classification model.
- `salaryregression.ipynb`: Contains the workflow for the Salary Regression model.

Both include Data Preprocessing, Feature Encoding, ANN Architecture Definition, and Training loops.
