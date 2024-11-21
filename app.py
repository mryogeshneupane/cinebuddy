from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    req = request.get_json()

    # Extract the intent name to check what the user is asking for
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName', '')

    # Student data (could be dynamic, like from a database)
    student_name = "Yogesh Neupane"
    student_id = "200570557"

    # Check if the user is asking for student details
    if intent == 'GetStudentDetails':
        response_text = f"The student name is {student_name}, and the student ID is {student_id}."

        # JSON Response to be sent back to Dialogflow
        response = {
            "fulfillmentText": response_text,  # Text that will be shown in the chat interface
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [response_text]  # This is the same text, but in a structured format
                    }
                }
            ],
            "payload": {
                "studentName": student_name,  # Custom data you can send in the payload
                "studentID": student_id
            },
            "source": "your-app-on-render"
        }

    else:
        response_text = "Sorry, I couldn't find the requested information."
        response = {
            "fulfillmentText": response_text,
            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [response_text]
                    }
                }
            ]
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
