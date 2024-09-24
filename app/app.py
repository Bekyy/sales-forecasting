from flask import Flask, request, jsonify, render_template_string
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
import io
import base64
import matplotlib.pyplot as plt

# Initialize Flask app
app = Flask(__name__)

# Load the serialized model with pipeline (replace with your actual model file)
model = joblib.load('./models/model-23-09-2024-21-30-57-720764.pkl')

# Define a route for home page with file upload form and result display
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            # Check if a file is included in the request
            if 'file' not in request.files:
                return jsonify({'error': 'No file part in the request'}), 400

            file = request.files['file']

            # Check if the file is CSV
            if file.filename == '':
                return jsonify({'error': 'No selected file'}), 400

            if not file.filename.endswith('.csv'):
                return jsonify({'error': 'Invalid file format. Please upload a CSV file.'}), 400

            # Read CSV into a DataFrame
            df = pd.read_csv(file)

            # Expected columns in the CSV
            expected_columns = ['Date', 'year', 'month', 'day', 'DayOfWeek', 'Store', 'Open', 'Promo', 'StateHoliday', 'SchoolHoliday',
                                'StoreType', 'Assortment', 'CompetitionDistance', 'CompetitionOpenSinceMonth',
                                'CompetitionOpenSinceYear', 'Promo2', 'Promo2SinceWeek', 'Promo2SinceYear']

            # Check if all expected columns are present
            if not all(col in df.columns for col in expected_columns):
                return jsonify({'error': 'Missing required columns in the CSV'}), 400

            # Ensure that the 'Date' column is in the correct datetime format
            df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

            # Check for invalid dates
            if df['Date'].isnull().any():
                return jsonify({'error': 'Invalid date format in the "Date" column'}), 400

            # Preprocess the data and make predictions using the model's pipeline
            predictions = model.predict(df[expected_columns].drop(columns=['Date']))

            # Add predictions to the DataFrame
            df['PredictedSales'] = predictions

            # Plotting the predictions
            plt.figure(figsize=(10, 6))
            plt.plot(df['Date'], df['PredictedSales'], marker='o', linestyle='-', color='b')
            plt.title('Predicted Sales Over Time')
            plt.xlabel('Date')
            plt.ylabel('Predicted Sales')
            plt.grid(True)
            plt.xticks(rotation=45)

            # Save the plot to a PNG image in memory (bytes)
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode('utf8')

            # Create HTML for displaying the table and the plot
            result_html = '''
            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <title>Sales Prediction API</title>
              </head>
              <body>
                <div style="text-align:center;">
                  <h1>Sales Predictions</h1>
                  <p>Upload your CSV file to get sales predictions.</p>
                  <form method="POST" enctype="multipart/form-data">
                    <input type="file" name="file" accept=".csv" required>
                    <button type="submit">Upload and Predict</button>
                  </form>
                  
                  <h2>Predicted Sales Data</h2>
                  <table border="1" style="margin: 0 auto; width: 80%;">
                    <tr>
                      <th>Date</th>
                      <th>Predicted Sales</th>
                    </tr>
                    {% for row in predictions %}
                    <tr>
                      <td>{{ row['Date'] }}</td>
                      <td>{{ row['PredictedSales'] }}</td>
                    </tr>
                    {% endfor %}
                  </table>

                  <h2>Predicted Sales Plot</h2>
                  <img src="data:image/png;base64,{{ plot_url }}" alt="Predicted Sales Plot">

                </div>
              </body>
            </html>
            '''
            
            # Pass predictions and plot URL to the HTML template
            return render_template_string(result_html, predictions=df[['Date', 'PredictedSales']].to_dict(orient='records'), plot_url=plot_url)

        except Exception as e:
            return jsonify({'error': str(e)})
    
    # HTML for the home page
    home_html = '''
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>Sales Prediction API</title>
      </head>
      <body>
        <div style="text-align:center;">
          <h1>Welcome to the Sales Prediction API</h1>
          <p>Upload your CSV file to get sales predictions.</p>
          <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file" accept=".csv" required>
            <button type="submit">Upload and Predict</button>
          </form>
        </div>
      </body>
    </html>
    '''
    
    return render_template_string(home_html)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
