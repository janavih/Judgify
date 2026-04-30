from flask import Flask, request, jsonify, render_template
from model import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    query = data.get("query")

    result = get_response(query)

    return jsonify({
        "law": result["law"],
        "explanation": result["explanation"],
        "steps": result["steps"]
    })

if __name__ == "__main__":
    app.run(debug=True)
