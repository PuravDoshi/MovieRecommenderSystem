import streamlit as st 
import pickle
import pandas as pd

movie_dict=pickle.load(open(r'/Users/puravdoshi/Downloads/MovieRecommenderSystem/movie_list.pkl','rb'))
similarity=pickle.load(open(r'/Users/puravdoshi/Downloads/MovieRecommenderSystem/similarity.pkl','rb'))
movies=pd.DataFrame(movie_dict)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_names = []
    for i in distances:
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names

st.title('Movie Recommender System')

option=st.selectbox("What movie do you want to watch?",movies['title'].values)

if(st.button("Recommend")):
    recommendations=recommend(option)
    for i in recommendations:
        st.write(i)
