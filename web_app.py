import streamlit as st
import requests

st.title("🎵 AI Music Recommendation System")

option = st.selectbox("Choose Recommendation Type:", ["Content-Based", "Collaborative Filtering"])

if option == "Content-Based":
    song_name = st.text_input("Enter a Song Name:")
    if st.button("Get Recommendations"):
        response = requests.get(f"http://127.0.0.1:5000/recommend/content?song={song_name}")
        st.write("Recommended Songs:", response.json()["recommended_songs"])

else:
    user_id = st.number_input("Enter User ID:", min_value=1, step=1)
    if st.button("Get Recommendations"):
        response = requests.get(f"http://127.0.0.1:5000/recommend/collaborative?user_id={user_id}")
        st.write("Recommended Songs:", response.json()["recommended_songs"])
