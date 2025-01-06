import streamlit as st
import pickle
import pandas as pd
import requests

def recommend(musics):
    music_index = music[music['title'] == musics].index[0]
    distances = similarity[music_index]
    music_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_music = []
    recommended_music_poster = []
    for i in music_list:
        music_title = music.iloc[i[0]].title
        recommended_music.append(music.iloc[i[0]].title)
        #recommended_music_poster.append(fetch_poster(music_title))
    return recommended_music#, recommended_music_poster

music_dict = pickle.load(open('data/musicrec.pkl', 'rb'))
music = pd.DataFrame(music_dict)
#covers_dict = pickle.load(open('covers.pkl', 'rb'))
#covers = pd.DataFrame(covers_dict)

similarity = pickle.load(open('data/similarities.pkl', 'rb'))

st.title('Music Recommendation System')

selected_music_name = st.selectbox('Select an album that you like', music['title'].values)

if st.button('Recommend'):
    names = recommend(selected_music_name)
    #names, posters = recommend(selected_music_name)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        #st.image(posters[0])
    with col2:
        st.text(names[1])
        #st.image(posters[1])
    with col3:
        st.text(names[2])
        #st.image(posters[2])
    with col4:
        st.text(names[3])
        #st.image(posters[3])
    with col5:
        st.text(names[4])
        #st.image(posters[4])



