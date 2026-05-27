from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/count", methods=["POST"])
def count_chars():
    data = request.get_json()
    text = data.get("text", "")

    return jsonify({
        "count": len(text)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

