# Air Quality Index (AQI) Prediction

## 📌 Project Description
Air pollution is a critical issue affecting health and the environment. This project aims to predict the **Air Quality Index (AQI)** based on various pollutant concentrations using a machine learning model. The system is developed as a **Streamlit web application**, where users can enter air quality parameters and receive an AQI prediction along with health impact insights.

---

## 🚀 Features
- **Machine Learning Model** trained on air quality data.
- **Web-based Prediction Interface** using **Streamlit**.
- **User Input Fields** for pollutant levels.
- **AQI Classification** (Good, Moderate, Unhealthy, Hazardous, etc.).
- **Health Awareness Messages** based on AQI.

---

## 📊 Dataset Information
The dataset contains multiple air pollutants as features, including:
- **PM2.5** (Particulate Matter < 2.5μm)
- **PM10** (Particulate Matter < 10μm)
- **NO, NO2, NOx** (Nitrogen Oxides)
- **SO2** (Sulfur Dioxide)
- **NH3** (Ammonia)
- **CO** (Carbon Monoxide)
- **O3** (Ozone)
- **Benzene, Toluene, Xylene** (Volatile Organic Compounds)

The AQI values are used as labels for training the model.

---

## 🛠️ Tools & Technologies Used
- **Python** (Data Processing & Model Building)
- **Pandas, NumPy** (Data Manipulation & Analysis)
- **Scikit-learn** (Machine Learning)
- **Pickle** (Model Serialization)
- **Streamlit** (Web Application Development)

---

## ⚙️ Model Description
The project uses a **machine learning regression model** to predict AQI values based on pollutant concentrations. The model is trained and stored in a **Pickle file (AIR_QUALITY_INDEX.pkl)**.

### **Preprocessing & Model Steps:**
1. **Data Cleaning:** Handled missing values & outliers.
2. **Feature Scaling:** Used `X_scaler.pkl` for input features and `y_scaler.pkl` for AQI output.
3. **Model Training:** Trained using a regression model.
4. **Model Saving:** Saved the trained model as a `.pkl` file.
5. **Prediction Flow:**
   - User inputs pollutant values.
   - Inputs are scaled using `X_scaler.pkl`.
   - Model predicts AQI.
   - Output AQI is inverse-scaled using `y_scaler.pkl`.
   - Display results with appropriate health warnings.

---

# 📊 Model Performance Summary

## 🌟 Random Forest Regression
👉 **Best overall model** – Achieves an optimal balance between training and testing performance.

### Training Performance:
- **Mean Squared Error (MSE):** `0.0011` (🔹 Extremely low, indicating an almost perfect fit.)
- **R² Score:** `0.9779` (🔹 High variance explanation and model reliability.)
- **Mean Absolute Error (MAE):** `0.0209` (🔹 Minimal training error.)

### Testing Performance:
- **MSE:** `0.0079` (🔹 Lowest among all models, signifying superior predictive accuracy.)
- **R² Score:** `0.8454` (🔹 Highest among all models, demonstrating strong generalization capability.)
- **MAE:** `0.0556` (🔹 Low test error, reinforcing robustness.)

---

## 🚀 Gradient Boosting Regression
👉 **Second-best model** – Provides good generalization but is slightly outperformed by Random Forest.

### Training Performance:
- **MSE:** `0.0088`
- **R² Score:** `0.8291`
- **MAE:** `0.0627`

### Testing Performance:
- **MSE:** `0.0089`
- **R² Score:** `0.8257`
- **MAE:** `0.0636`

🔍 **Observation:** Performs well but falls short of Random Forest in both training and testing metrics.

---

## ❌ Decision Tree Regression
⚠️ **Significant overfitting detected** – High training accuracy but poor generalization to unseen data.

### Training Performance:
- **MSE:** `0.00003` (⚠️ Extremely low, indicating potential memorization rather than learning patterns.)
- **R² Score:** `0.9993` (⚠️ Unusually high, suggesting an overfitted model.)
- **MAE:** `0.0002`

### Testing Performance:
- **MSE:** `0.0158` (⚠️ High error, confirming poor generalization.)
- **R² Score:** `0.6891` (⚠️ Noticeably lower than Random Forest and Gradient Boosting.)
- **MAE:** `0.0763`

🔍 **Observation:** While the model excels in training, its high test error makes it **unsuitable for real-world deployment**.

---

## ✅ Final Conclusion
📌 **Random Forest Regression emerges as the best-performing model**, offering the highest accuracy and generalization capability.  
📌 **Gradient Boosting Regression follows closely** and remains a viable alternative.  
📌 **Decision Tree Regression suffers from overfitting**, making it unsuitable for deployment.  

---

## 🖥️ Installation & Running Steps
### **Step 1: Clone the Repository**
```bash
git clone https://github.com/narevignesh/AQI_Prediction.git
cd AQI_Prediction
```

### **Step 2: Install Required Dependencies**
Ensure you have Python installed (preferably **Python 3.8+**), then install the required libraries:
```bash
pip install -r requirements.txt
```

### **Step 3: Run the Jupyter Notebook**
Before running the app, execute all cells in the Jupyter Notebook to preprocess data and train the model:
```bash
jupyter notebook Air_Quality_Index.ipynb
```
Run all cells in the notebook to ensure the model is trained and saved correctly.

### **Step 4: Run the Streamlit App**
```bash
streamlit run app.py
```

This will start a local web server where you can interact with the AQI prediction model.

---

### 🌍 Breathe fresh, live healthy! 🚀

