Files in the Repository
training.ipynb: Jupyter Notebook used for data preprocessing and training the machine learning model using linear regression.

flask_app: This Flask code initializes an API endpoint /predict that receives a POST request containing JSON data for predicting values based on a loaded machine learning model trained using Pandas and Pickle, returning the predicted result in a JSON format.

app.py: utilizes the requests library in Python to perform a POST request to a local server (http://127.0.0.1:5000/predict) with JSON data loaded from a file named data.json, printing the prediction response if the request succeeds or displaying a failure message with the corresponding status code.

