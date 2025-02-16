from flask import Flask, request, jsonify
from recommendation import content_based_recommend, collaborative_recommend

app = Flask(__name__)

@app.route("/recommend/content", methods=["GET"])
def recommend_content():
    song_name = request.args.get("song")
    recommendations = content_based_recommend(song_name)
    return jsonify({"recommended_songs": recommendations})

@app.route("/recommend/collaborative", methods=["GET"])
def recommend_collaborative():
    user_id = int(request.args.get("user_id"))
    recommendations = collaborative_recommend(user_id)
    return jsonify({"recommended_songs": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
