from flask import Flask, request, jsonify

app = Flask(__name__)

#route to return student name and student number
@app.route('/')
def home():
    return jsonify({
        "student_full_name": "Yogesh Neupane",
        "student_number": "200570557"
    })

#fulfillment route
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    #get the intent name
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName', '')

    #response for fulfillment
    if intent == 'FulfillmentIntent':
        response_text = "This is a response from the Flask webhook!"
    else:
        response_text = "Fallback response"

    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)