# 🫀 Heart Failure Prediction using MLP + Streamlit

This is a simple machine learning app that predicts the risk of a death event in heart failure patients.  
Built with **MLP Neural Network**, trained on a clinical dataset, and deployed using **Streamlit**.

---

## 📊 Dataset

- Used the [heart_failure_clinical_records_dataset]
- Target variable: `DEATH_EVENT`  
- Features: Age, Anaemia, Creatinine Phosphokinase, Diabetes, Ejection Fraction, etc.

---

## 🧠 Model

- Built using **Multi-Layer Perceptron (MLP)** from TensorFlow/Keras
- Trained to classify if a patient is likely to have a death event
- Preprocessing included standard scaling using `StandardScaler`

---

## 🖥️ App Features

- Built with `streamlit`
- Takes user input for clinical values
- Predicts death risk in real-time using the trained model

---

## 📦 Requirements

Install all dependencies using:

Google Collab Link
[https://colab.research.google.com/drive/1V1LHX3iskr9snS6n-RyBImFNGB0f3bYp?usp=sharing]

```bash
pip install -r requirements.txt
