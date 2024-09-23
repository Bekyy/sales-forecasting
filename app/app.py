from flask import Flask, request, jsonify
import joblib
import numpy as np
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Load the serialized model (replace 'model_filename.pkl' with your actual model file)
model = joblib.load('./models/model-23-09-2024-21-30-57-720764.pkl')

# Define a route for home or health check (optional)
@app.route('/')
def home():
    return "Welcome to the Sales Prediction API. Use the /predict endpoint for predictions."

# Define prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        input_data = request.json  # Expecting input as JSON
        
        # Convert input data into the format the model expects
        # Assuming input_data is a list or single instance that needs to be converted to a 2D array
        data = np.array([input_data])
        
        # Make prediction using the loaded model
        prediction = model.predict(data)
        
        # Format the response
        response = {
            'input': input_data,
            'prediction': prediction.tolist(),
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
