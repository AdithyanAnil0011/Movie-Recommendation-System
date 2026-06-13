
https://movie-recommendation-system-5ht7d2dwzpebvuuejbpp7a.streamlit.app/
📌 Features
🎥 Movie recommendation based on similarity
🖼️ Dynamic movie posters using OMDb API
🎨 Modern dark-themed UI with hover card effects
⚡ Fast recommendation generation
📱 Responsive Streamlit layout
🔍 Content-based filtering using NLP techniques





# 🎬 Movie Recommendation System

A content-based Movie Recommendation System built using **Streamlit**  powered by a **Machine Learning** and uses the **OMDb API** for Fetching Movie posters.
The application recommends movies similar to the one selected by the user using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 🚀 Live Demo

🔗 https://movie-recommendation-system-5ht7d2dwzpebvuuejbpp7a.streamlit.app/

---

## 📌 Features

* 🎥 Movie recommendation based on similarity
* 🖼️ Dynamic movie posters using OMDb API
* 🎨 Modern dark-themed UI with hover card effects
* ⚡ Fast recommendation generation
* 📱 Responsive Streamlit layout
* 🔍 Content-based filtering using NLP techniques

---

## 🛠️ Tech Stack

### Frontend

* Streamlit
* HTML/CSS

### Backend / ML

* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

### API

* OMDb API

---

## 🧠 Machine Learning Workflow

1. Movie dataset preprocessing
2. Feature selection:

   * Genres
   * Keywords
   * Cast
   * Overview
3. Text feature combination
4. TF-IDF vectorization
5. Cosine similarity computation
6. Recommendation generation

---

## 📂 Project Structure

```bash
Movie-Recommendation-System/
│
├── app.py
├── home_page.jpg
├── moviesdata.csv
├── movie_dict.pkl
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🎯 How It Works

The system recommends movies based on content similarity rather than popularity or ratings.

It analyzes movie metadata such as:

* genres
* cast
* keywords
* overview

Then converts the text into numerical vectors using TF-IDF and calculates similarity scores using cosine similarity.

---

## 📸 Screenshots

Add screenshots of your app here.

---

## 🔮 Future Improvements

* Add IMDb ratings
* Add movie trailers
* Improve recommendation quality using embeddings
* Add fuzzy search
* Deploy optimized cached model
* User authentication and watchlist support

---

## 🙌 Acknowledgements

* OMDb API
* Streamlit
* Scikit-learn
* TMDB/IMDb datasets

---

## 👨‍💻 Author

**Adithyan Anilkumar**

Feel free to connect with me on LinkedIn and GitHub.
* Linkedin:https://www.linkedin.com/in/adithyan-anilkumar-a23129329/
