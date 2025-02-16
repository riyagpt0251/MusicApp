import streamlit as st
import requests
import pandas as pd

# Spotify API Credentials (Replace with your own)
CLIENT_ID = "c34a35abaf12452e9cdbe2a2538b2c54"
CLIENT_SECRET = "322d9d2d31e7428797780dc13d1efc42"

# Streamlit UI
st.set_page_config(page_title="AI Music Recommendation", layout="wide")
st.title("🎵 AI Music Recommendation System")

# Sidebar Menu
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Spotify_logo_with_text.svg/1920px-Spotify_logo_with_text.svg.png", width=200)
st.sidebar.header("🔍 Search & Explore")
search_query = st.sidebar.text_input("Enter a song or artist:")

# Recommendation Type
st.sidebar.header("🎧 Recommendation Type")
option = st.sidebar.radio("Choose an option:", ["Content-Based", "Collaborative Filtering"])

# Search & Fetch Data from API
def fetch_spotify_data(query):
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer YOUR_ACCESS_TOKEN"}
    params = {"q": query, "type": "track", "limit": 5}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    return None

if search_query:
    st.subheader(f"🔎 Search Results for '{search_query}'")
    data = fetch_spotify_data(search_query)
    if data:
        for track in data["tracks"]["items"]:
            st.write(f"🎶 {track['name']} by {track['artists'][0]['name']}")
            st.image(track['album']['images'][0]['url'], width=150)
    else:
        st.error("❌ No results found!")

if option == "Content-Based":
    song_name = st.text_input("Enter a Song Name for Recommendations:")
    if st.button("Get Recommendations"):
        if not song_name.strip():
            st.warning("⚠️ Please enter a song name.")
        else:
            try:
                response = requests.get(f"http://localhost:5000/recommend/content?song={song_name}")
                if response.status_code == 200:
                    st.success("✅ Here are your recommendations:")
                    st.write(response.json()["recommended_songs"])
                else:
                    st.error("❌ No recommendations found. Check the song name.")
            except requests.exceptions.ConnectionError:
                st.error("❌ Failed to connect to the recommendation API. Ensure the Flask server is running.")

else:
    user_id = st.number_input("Enter User ID:", min_value=1, step=1)
    if st.button("Get Recommendations"):
        try:
            response = requests.get(f"http://127.0.0.1:5000/recommend/collaborative?user_id={user_id}")
            if response.status_code == 200:
                st.success("✅ Here are your recommendations:")
                st.write(response.json()["recommended_songs"])
            else:
                st.error("❌ No recommendations found for this user.")
        except requests.exceptions.ConnectionError:
            st.error("❌ Failed to connect to the recommendation API. Make sure the Flask server is running.")
