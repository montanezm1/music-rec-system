import random

def recommend(album_title, df, cosine_sim, top_n=5):
    # Find the index of the given album
    idx = df.index[df['album'].str.lower() == album_title.lower()].tolist()
    if not idx:
        return f"Album '{album_title}' not found."
    idx = idx[0]
    
    # Get similarity scores for this album
    sim_scores = list(enumerate(cosine_sim[idx]))
    
    # Sort albums by similarity (highest first)
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Skip the first one (it's the same album)
    sim_scores = sim_scores[1:]  
    
    # Top N most similar albums
    top_recs = []
    for i, score in sim_scores[:top_n]:
        top_recs.append({
            "album": df.iloc[i]['album'],
            "artist": df.iloc[i]['artist'],
            "cover": df.iloc[i]['cover'],
            "similarity": round(score, 3)  # optional to show similarity score
        })
    
    # Pick 1 random album from all albums
    random_pool = sim_scores[top_n:]
    random_pick = None
    if random_pool:
        i, score = random.choice(random_pool)
        random_pick = {
            "album": df.iloc[i]['album'],
            "artist": df.iloc[i]['artist'],
            "cover": df.iloc[i]['cover'],
            "similarity": round(score, 3)
        }

    return {
        "most_similar": top_recs,
        "random_related": random_pick,
    }


