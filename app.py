from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    
    # Get the intent name
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName', '')
    
    # Default student data (replace with actual data or a database lookup if needed)
    student_name = "Yogesh Neupane"
    student_id = "200570557"
    
    # Create a response based on the intent
    if intent == 'FulfillmentIntent':
        response_text = f"The student name is {student_name}, and the ID is {student_id}."
    else:
        response_text = "Fallback response"
    
    # Build the JSON response
    return jsonify({
        "fulfillmentText": response_text,
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [response_text]
                }
            }
        ],
        "payload": {
            "studentName": student_name,
            "studentID": student_id
        },
        "source": "your-app-on-render"
    })

if __name__ == '__main__':
    app.run(debug=True)
