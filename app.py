import pandas as pd
import streamlit as st
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

tracks = pd.read_csv(r'C:\Users\naman\tracks2.csv')

song_vectorizer = CountVectorizer()
song_vectorizer.fit(tracks['track_genre'])

songs_dict = pickle.load(open('songs_dict.pkl', 'rb'))
songs = pd.DataFrame(songs_dict)

similarity_matrix = np.array(pickle.load(open('similarity2.pkl', 'rb')))
similarity_matrix = similarity_matrix.reshape(-1, 1)

def get_similarities(song_name, data):
    text_array1 = song_vectorizer.transform(data[data['track_name'] == song_name]['track_genre']).toarray()
    num_array1 = data[data['track_name'] == song_name].select_dtypes(include=np.number).to_numpy()

    text_array2 = song_vectorizer.transform(data['track_genre']).toarray()
    num_array2 = data.select_dtypes(include=np.number).to_numpy()

    text_sim = cosine_similarity(text_array1, text_array2)
    num_sim = cosine_similarity(num_array1, num_array2)

    sim = text_sim + num_sim
    return sim.tolist()[0]

def recommend_songs(song_name, data=tracks):
    if data[data['track_name'] == song_name].shape[0] == 0:
        st.warning('This song is either not so popular or you have entered an invalid name. Some songs you may like:')
        recommendations = data.sample(n=5)[['track_name', 'artists']]
        st.markdown("**Recommendations:**")
        st.table(recommendations.reset_index(drop=True))
        return

    data['similarity_factor'] = get_similarities(song_name, data)

    data.sort_values(by=['similarity_factor', 'popularity'], ascending=[False, False], inplace=True)

    st.markdown("**Recommendations:**")
    st.table(data[['track_name', 'artists']][2:7].reset_index(drop=True))

st.title('Music Recommendation System')

selected_song_name = st.selectbox(
    'What would you want to listen today?',
    songs['track_name'].values
)

if st.button('Recommend'):
    recommend_songs(selected_song_name, tracks)
