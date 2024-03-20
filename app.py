from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    # Get features from request
    features = request.json['features']

    # Perform prediction
    prediction = model.predict([features])[0]

    # Return prediction
    return jsonify({'prediction': str(prediction)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
