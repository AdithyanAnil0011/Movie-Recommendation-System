
import streamlit as st
import pickle
import pandas as pd
import requests
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# APP Background Styling
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image:linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url("https://cdn.wallpapersafari.com/24/74/zgeTuV.jpg");
    background-size:cover;
    background-position:center;
    background-repeat:no-repeat;
    background-attachment:fixed;
}

[data-testid="stHeader"] {
    background:rgba(0,0,0,0);
}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)

selected_features=['genres','keywords','overview','cast','director']   #selected features for better recommendatiosn  

# Load Data Safely
movies = pd.read_csv("moviesdata.csv")

# similarity = pickle.load(open('similarity.pkl', 'rb'))   [Could not load similarity.pkl File directly to github since the file was too large]
for feature in selected_features:
    movies[feature] = movies[feature].fillna('')

combined_features=(movies['genres']+' '+movies['keywords']+' '+movies['overview']+' '+movies['cast']+' '+movies['director'])

vectorizer =TfidfVectorizer()
feature_vectors =vectorizer.fit_transform(combined_features)

similarity =cosine_similarity(feature_vectors)

# Fetch Movie Poster with API(Used OMDB API)
def fetch_poster(movie_name):
    movie_name = movie_name.replace(" ", "+")
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey=35ba7859"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        return data.get('Poster', "N/A")
    except Exception:
        return "N/A"

# Recommendation Logic
def recommend(movie):
    movie_index = movies[movies.title == movie].index[0]
    distances = similarity[movie_index]
    
    # Grabs top 9 recommendations
    movie_list = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:10]    # sorting on the basis of priority of movies
    
    recommended_movies = [] 
    recommended_posters = []
    
    for i in movie_list:
        movie_name = movies.iloc[i[0]].title
        recommended_movies.append(movie_name) 
        recommended_posters.append(fetch_poster(movie_name))
        
    return recommended_movies, recommended_posters

# UI Styling
st.markdown(""" <h1 style='text-align: left; color: white; font-size: 50px; font-weight: bold; margin-bottom: 30px;'> 🎬 Movie Recommendation System </h1> """, unsafe_allow_html=True)

st.markdown("""
<style>
/* Selectbox label styling */
div[data-testid="stSelectbox"] label p {
    font-size: 24px !important;
    font-weight: bold !important;
    color: white !important;
}

/* Dropdown styling */
div[data-baseweb="select"] > div {
    font-size: 18px !important;
}

/* FIXED MOVIE CARD CSS */
.movie-card {
    background-color: rgba(20,20,20,0.85);
    border-radius: 15px;
    padding: 12px;
    text-align: center;
    transition: all 0.3s ease;
    height: 480px; /* Reliable uniform height */
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-bottom: 25px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    border: 1px solid rgba(255,255,255,0.1);
}

.movie-card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 8px 25px rgba(255, 0, 0, 0.5);
    border: 1px solid rgba(255, 0, 0, 0.3);
}

.movie-card img {
    width: 100%;
    height: 82%; /* Uses percentages so title has guaranteed space */
    object-fit: cover;
    border-radius: 10px;
}

.movie-title {
    color: white;
    font-size: 16px;
    font-weight: bold;
    height: 15%; /* Allocated space for text */
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    text-overflow: ellipsis;
}
</style>
""", unsafe_allow_html=True)

# Input from the user
selected_movie = st.selectbox(
    'Enter the name of your Favourite Movie',
    movies['title'].values
)

if st.button('Recommend'):
 placeholder = st.empty()
 with st.spinner('Fetching movie recommendations...'):
     name, posters = recommend(selected_movie)
    # Create 3 rows of 3 columns
     for i in range(0, len(name), 3):
        cols = st.columns(3)
        for j in range(3):
            idx = i + j
            if idx < len(name):
                with cols[j]:
                    poster_url = posters[idx]
                    # if API response is empty or N/A
                    if poster_url == "N/A" or not poster_url:
                        poster_url = "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?q=80&w=400"

                    st.markdown(f"""
                    <div class="movie-card">
                        <img src='{poster_url}'>
                        <div class="movie-title">
                            {name[idx]}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
