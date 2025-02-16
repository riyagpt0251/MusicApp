import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Sample dataset
music_data = pd.DataFrame({
    'title': ['Song A', 'Song B', 'Song C', 'Song D'],
    'genre': ['Rock', 'Pop', 'Jazz', 'Rock'],
    'artist': ['Artist 1', 'Artist 2', 'Artist 3', 'Artist 1']
})

# Content-Based Filtering
def content_based_recommend(song_title):
    tfidf = TfidfVectorizer()
    genre_matrix = tfidf.fit_transform(music_data['genre'])
    similarity = cosine_similarity(genre_matrix)

    index = music_data[music_data['title'] == song_title].index[0]
    scores = list(enumerate(similarity[index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    recommendations = [music_data.iloc[i[0]]['title'] for i in scores[1:]]
    return recommendations

# Collaborative Filtering (Dummy Function)
def collaborative_recommend(user_id):
    return ["Song X", "Song Y", "Song Z"]
