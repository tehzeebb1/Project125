from flask import Flask, jsonify, request
from classifier import  get_prediction
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/predict-digit", methods=["POST"])
def predict_data():
  image = request.files.get("digit")
  prediction = get_prediction(image)
  return jsonify({
    "prediction": prediction
  }), 200

if __name__ == "__main__":
  app.run(debug=True)