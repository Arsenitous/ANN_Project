# 🏦 Customer Churn Prediction (Deep Learning ANN)

Welcome to the Customer Churn Prediction project! This application utilizes an Artificial Neural Network (ANN) to predict whether a bank customer is likely to leave (churn) or stay based on their profile.

🚀 **[Try the Live Web App Here!](https://annproject-5zctv7sjdshcazkdec6aut.streamlit.app/)**

---

## 📖 Overview
Customer churn is a critical metric for financial institutions. This deep learning model analyzes various customer features—such as Geography, Gender, Age, Credit Score, and Account Balance—to accurately calculate the probability of a customer exiting the bank.

The interactive web interface is built using **Streamlit**, providing a user-friendly way to input customer details and instantly receive a prediction.

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

4. **Run the Streamlit App:**
   ```bash
   streamlit run app.py
   ```

5. **View the App:**
   Open your browser and navigate to `http://localhost:8501`.

## 📊 Model Training
If you want to see how the model was built and trained, check out the `experiments.ipynb` notebook. It contains the complete workflow:
- Data Preprocessing & Scaling
- Feature Encoding
- ANN Architecture Definition
- Training loop with TensorBoard integration
