Text Emotion Classification API

This Flask application provides an API endpoint for classifying the emotion of a given text using a pre-trained DistilBERT-based model. The model predicts the emotion of the input text among several predefined emotion labels.

Setup
To set up this project locally, follow these steps:

Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/your-repo.git

Navigate to the project directory:
bash
Copy code
cd your-repo

Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
Usage

To use the API, run the Flask application:

bash
Copy code
python app.py
The API will start running locally at http://127.0.0.1:5000/. You can send POST requests to this endpoint with a JSON payload containing the text to be classified.

Example request:

bash
Copy code
curl -X POST http://127.0.0.1:5000/ -H "Content-Type: application/json" -d '{"text": "I feel so happy today!"}'
Example response:

json
Copy code
{
    "label": "joy"
}
API Endpoint
POST /
Request Body: JSON
text: The text to be classified for emotion.
Response: JSON
label: The predicted emotion label for the input text.
Model Details
The emotion classification model used in this project is based on DistilBERT and is fine-tuned on an emotion classification task.

The model predicts the emotion of the input text among the following emotion labels:

joy
sadness
anger
fear
surprise
love

Contributors:
HUMZA WAQAR

License
This project is licensed under the MIT License - see the LICENSE file for details.
