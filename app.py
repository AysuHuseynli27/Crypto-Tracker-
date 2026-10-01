from flask import Flask, jsonify, render_template
from cryptotracker import CryptoPipeline

app = Flask(__name__)
pipe = CryptoPipeline()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/prices")
def prices():
    df = pipe.process_data(pipe.fetch_data())
    if df is None:
        return jsonify({"error": "Data alınmadı"}), 503
    pipe.save_to_db(df)
    return jsonify(df.to_dict(orient="records"))

if __name__ == "__main__":
    app.run(debug=True)
