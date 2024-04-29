from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Define the model to be used for classification
model_name = 'bhadresh-savani/distilbert-base-uncased-emotion'
classifier = pipeline("text-classification", model=model_name, return_all_scores=True)

# Function to make predictions using the model
def model_call(text):
    prediction = classifier(text)
    return prediction

@app.route('/', methods=['POST'])
def home():
    # Get input data from the request
    data = request.json

    if 'text' in data:

        text = data['text']

        prediction = model_call(text)
        prediction = prediction[0]
        # print(prediction)
        highest_score = prediction[0]['score']
        highest_score_label = prediction[0]['label']

        for i in range(1,len(prediction)):
            if highest_score < prediction[i]['score']:
                highest_score = prediction[i]['score']
                highest_score_label = prediction[i]['label']



        response_data = {"label": highest_score_label}
        return jsonify(response_data)
    
    else:
    
        return jsonify({'error': 'Text key input is missing'}), 400

if __name__ == '__main__':
    app.run(debug=True)
