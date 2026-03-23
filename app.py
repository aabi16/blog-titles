from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "Blog Title Generator Running 🚀"}

@app.route("/generate", methods=["POST"])
def generate_titles():
    data = request.get_json()

    if not data or "topic" not in data:
        return jsonify({"error": "Enter topic"}), 400

    topic = data["topic"]

    # Simple AI-like titles (no API)
    titles = [
        f"Top 10 Things to Know About {topic}",
        f"The Future of {topic}",
        f"Why {topic} is Trending Now",
        f"Beginner's Guide to {topic}",
        f"Everything About {topic} in 2026"
    ]

    return jsonify({
        "titles": "\n".join(titles)
    })


if __name__ == "__main__":
    app.run(debug=True)
