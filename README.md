# Music Rec System

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35.0-orange?logo=streamlit&logoColor=white)](https://streamlit.io/)  

A **machine learning-based music recommendation engine** that suggests albums based on genres, artist stats, record labels, album ratings, etc. — all in a **simple, interactive web app** built with Streamlit.  

---

## 🚀 Demo

Try it live: [Run on Streamlit Cloud](https://musicrecsystem.streamlit.app/)  

---

## 🔍 Features

- Personalized **Top-N recommendations** based on cosine similarity.  
- **Random related album pick** for music discovery.  
- **Interactive Streamlit UI** with album covers.  
- Uses **numeric + categorical features** (genres, labels, ratings, release year).  

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python, Pandas, NumPy  
- **Machine Learning:** Scikit-Learn (CountVectorizer, MinMaxScaler, cosine similarity)  
- **Dataset:** 2000+ albums extracted from Musicboard  

---

## 📦 Quick Start

1. Clone the repository:
```bash
git clone https://github.com/montanezm1/music-rec-system.git
cd music-rec-system

2. Install dependencies
```bash
pip install -r requirements.txt

3. Run the app
```bash
streamlit run app.py
