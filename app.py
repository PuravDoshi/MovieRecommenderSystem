import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(page_title="🎬 Movie Recommender", page_icon="🎥", layout="wide")

movie_dict = pickle.load(open(r'/Users/puravdoshi/Downloads/MovieRecommenderSystem/movie_list.pkl', 'rb'))
similarity = pickle.load(open(r'/Users/puravdoshi/Downloads/MovieRecommenderSystem/similarity.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

def fetch_poster(movie_title):
    api_key = "" 
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={movie_title}"
        response = requests.get(url)
        data = response.json()
        if data.get('results'):
            poster_path = data['results'][0].get('poster_path')
            if poster_path:
                return f"https://image.tmdb.org/t/p/w500{poster_path}"
        return None
    except:
        return None

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:4]  # top 3
    recommended_movies = [movies.iloc[i[0]].title for i in distances]
    return recommended_movies

st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.write("### Discover movies similar to your favorites!")

option = st.selectbox("🎞️ Choose a movie you like:", movies['title'].values)

if st.button("🔍 Get Recommendations"):
    recommendations = recommend(option)
    st.markdown("---")
    st.subheader("✨ Recommended Movies for You:")

    cols = st.columns(3)
    for idx, movie in enumerate(recommendations):
        poster_url = fetch_poster(movie)
        with cols[idx]:
            if poster_url:
                st.image(poster_url, width=200)  
            st.markdown(f"<div style='text-align:center; font-weight:600; color:#333;'>🎥 {movie}</div>", unsafe_allow_html=True)

st.markdown("""
    <hr>
    <div style='text-align: center; color: gray;'>
        Developed with ❤️ using <b>Streamlit</b> | Purav Doshi
    </div>
""", unsafe_allow_html=True)
