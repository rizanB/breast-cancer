from flask import Flask, render_template, request, jsonify
import pickle
from feature_model_list import feature_list_with_test_values, model_list

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    selected_model = request.form['selected_model']

    with open(f"trained_models/{selected_model}", 'rb') as file:
        model = pickle.load(file)

    input_data = {
        feature: float(request.form[feature])
        for feature in feature_list_with_test_values["benign"] 
    }

    prediction = model.predict([list(input_data.values())])

    prediction_value = prediction[0].item() if hasattr(prediction[0], 'item') else int(prediction[0])

    return jsonify({'selectedModel': selected_model,'prediction': prediction_value})

@app.route("/")
def home():
    return render_template("index.html", feature_list_with_test_values=feature_list_with_test_values, model_list=model_list)

if __name__ == "__main__":
    app.run(debug=True)