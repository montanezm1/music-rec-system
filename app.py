import streamlit as st
import pandas as pd
import pickle
from recommender import recommend  

# Load data and similarity matrix
df = pd.read_csv("./data/ratings_data.csv")  # your albums DataFrame
with open("./data/cosine_sim.pkl", "rb") as f:
    cosine_sim = pickle.load(f)

# Streamlit App
st.set_page_config(page_title="Album Recommender", layout="wide")

st.title("Album Recommendation System")

# Input box or dropdown for album selection
album_list = df['album'].tolist()
album_list = [""] + album_list  
selected_album = st.selectbox("Select an Album:", album_list, index=0)

if st.button("Recommend"):
    recs = recommend(selected_album, df, cosine_sim, top_n=5) # 5 albums recommended (n)

    # Display most similar albums
    st.subheader("Top Recommendations")
    cols = st.columns(5)
    for idx, r in enumerate(recs["most_similar"]):
        with cols[idx % 5]:
            st.image(r["cover"], width=150)
            st.markdown(f"**{r['album']}**")
            st.caption(f"by {r['artist']}")

    # Display random related album
    if recs["random_related"]:
        st.subheader("Random Related Pick")
        r = recs["random_related"]
        st.image(r["cover"], width=200)
        st.markdown(f"**{r['album']}**")
        st.caption(f"by {r['artist']}")
