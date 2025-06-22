from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)

# Set OpenAI API key (from Replit secret later)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Route for homepage
@app.route("/")
def home():
    return render_template("index.html")

# Route for handling AI requests
@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    message = data.get("message", "")

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o",  # or "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": (
                "You are a helpful financial assistant. "
                "You do not provide personal investment advice, but explain general options "
                "for beating inflation based on country, goals, and savings. Always include a disclaimer."
            )},
            {"role": "user", "content": message}
        ]
    )

    reply = response.choices[0].message.content
    return jsonify({"reply": reply})

# Run on Replit
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
