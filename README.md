# 🏠 House Price Prediction

A machine learning–based real estate price prediction system built using a **scikit-learn pipeline** and an **interactive Streamlit web application**.  
The project predicts house prices based on **location, total square feet, BHK, and number of bathrooms**.

---

## 📌 Overview

This project demonstrates an **end-to-end machine learning workflow**, from preprocessing and model training to deployment using Streamlit.  
It focuses on correct handling of numerical and categorical features and avoids common ML deployment mistakes.

---

## 🚀 Features

- End-to-end **Machine Learning Pipeline** using scikit-learn  
- Automatic preprocessing with `ColumnTransformer`
- Handles numerical and categorical features correctly
- Interactive **Streamlit UI** for real-time predictions
- Input validation for realistic predictions (BHK vs sqft)
- Clean and simple user interface

---

## 🛠️ Tech Stack

- Python  
- NumPy  
- Pandas  
- Scikit-learn  
- Streamlit  

---

## 📁 Project Structure

```
real_estate_price_prediction/
│
├── dataset/
│   ├── bengaluru_house_prices.csv
│   └── cleaned_bengaluru_house_prices.csv
│
├── model/
│   ├── .ipynb_checkpoints/
│   ├── columns.json
│   └── RidgeModel.pkl
│
├── notebook/
│   └── model.ipynb
│
├── server/
│   └── app.py
│
├── venv/
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone <your-github-repo-link>
cd real_estate_price_prediction
```

### 2. Create and activate virtual environment

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**Mac / Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run server/app.py
```

The app will open in your browser at:

```
http://localhost:8501
```

---

## 🧠 Learning Outcomes

- Understanding scikit-learn pipelines in real-world projects
- Correct handling of training vs inference data formats
- Deploying ML models using Streamlit
- Building ML applications without frontend frameworks

---

## 🔮 Future Improvements

- Improve model accuracy with feature engineering
- Add confidence intervals for predictions
- Deploy on Streamlit Cloud
- Add data visualizations

---

## ⭐ If you found this project useful, consider giving it a star!
