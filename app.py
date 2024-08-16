from flask import Flask, render_template, request, jsonify
import pickle
from feature_model_list import feature_list_with_test_values, model_list

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the selected model filename from the form data
    selected_model = request.form['selected_model']

    # Load the selected model using pickle
    with open(f"trained_models/{selected_model}", 'rb') as file:
        model = pickle.load(file)

    # Get the input data from the form based on the selected case type
    input_data = {
        feature: float(request.form[feature])
        for feature in feature_list_with_test_values["benign"]  # Use the selected case type to get features
    }

    # Make a prediction using the loaded model
    prediction = model.predict([list(input_data.values())])

    # Convert the prediction to a standard Python type
    prediction_value = prediction[0].item() if hasattr(prediction[0], 'item') else int(prediction[0])

    # Return the prediction as a JSON response
    return jsonify({'selectedModel': selected_model,'prediction': prediction_value})

@app.route("/")
def home():
    return render_template("index.html", feature_list_with_test_values=feature_list_with_test_values, model_list=model_list)

if __name__ == "__main__":
    app.run(debug=True)