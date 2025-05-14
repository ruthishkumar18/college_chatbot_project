from flask import Flask, render_template, request, jsonify
from chatbot_model import predict_intent

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    user_input = request.form['message']
    response = predict_intent(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
