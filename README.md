# 🎬 Movie Recommender System

A personalized **Movie Recommender System** built using **Collaborative Filtering** on the **TMDB 5000 Movies Dataset**.  
This project suggests movies similar to user preferences and displays them in an **interactive Streamlit dashboard** with movie posters and metadata.

---

## 🚀 Overview

The recommender system predicts user-movie interactions based on collaborative filtering principles.  
It leverages user ratings and similarities between movies to generate personalized recommendations.

The **Streamlit dashboard** provides an intuitive interface to:
- Search for any movie
- View top 5 recommended movies
- See movie posters for a rich user experience

---

## 🧠 How It Works

1. **Data Source:**  
   - Dataset: TMDB 5000 Movies Dataset
   - Preprocessing includes feature extraction (genres, keywords, cast, crew) and vectorization.

2. **Model Used:**  
   - **Collaborative Filtering (TF-IDF Vectorization)** based on movie metadata and user interactions.
   - Recommends similar movies by calculating the cosine similarity between movie vectors.

3. **Dashboard:**  
   - Built using **Streamlit** for interactivity.
   - Fetches **movie posters dynamically** using TMDB API.
   - Clean and minimalistic UI for seamless recommendations.

---

## 📊 Features

✅ Search any movie and get **top 5 similar recommendations**  
✅ Interactive **Streamlit dashboard** with real-time results  
✅ **Poster and metadata integration** for an enhanced user experience  
✅ Fast, light, and easy to use locally or deploy online  

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Language** | Python |
| **Framework** | Streamlit |
| **Libraries** | pandas, numpy, scikit-learn, requests, pickle |
| **Model** | Collaborative Filtering (TF-IDF Vectorization) |
| **Dataset** | TMDB 5000 Movies |

---

## 🗂️ Project Structure

```bash
Movie_Recommender/
├── app.py                # Streamlit dashboard
├── model.ipynb        # Core recommendation logic
├── tmdb_5000_movies.csv  # Movie dataset
├── tmdb_5000_credits.csv # Cast and crew dataset
└── README.md             # Project documentation
```
