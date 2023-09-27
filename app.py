import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=25f03c5774573c29b1743cd195e8df15'.format(movie_id))
    data = response.json()

    if 'poster_path' in data:
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    else:
        return None  # Return None if poster_path is not found in the API response

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movie_posters =[]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommend_movies.append(movies.iloc[i[0]].title)
        # fetch posters from movies
        recommend_movie_posters.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movie_posters

movie_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity =pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Search for a movie',movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3 ,col4 , col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])
# def recommend(movie):
#     movie_index = movies[movies["title"] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommend_movies = []
#     recommend_movie_posters = []
#     for i in movies_list:
#         movie_id = i[0]
#         recommended_movie = movies.iloc[i[0]].title
#         poster_url = fetch_poster(movie_id)
#
#         if poster_url is not None:
#             recommend_movies.append(recommended_movie)
#             recommend_movie_posters.append(poster_url)
#
#     return recommend_movies, recommend_movie_posters
#
# # Streamlit code for displaying recommended movies and posters
# if st.button('Recommend'):
#     names, posters = recommend(selected_movie_name)
#
#     if names and posters:  # Check if there are recommended movies and posters
#         col1, col2, col3 = st.columns(3)
#
#         with col1:
#             st.header(names[0])
#             st.image(posters[0])
#
#         with col2:
#             st.header(names[1])
#             st.image(posters[1])
#
#         with col3:
#             st.header(names[2])
#             st.image(posters[2])
