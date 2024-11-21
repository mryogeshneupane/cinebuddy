import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

API_KEY = "b764bbac7bc7d741dd67077fb897e371"  
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather"

#route to return student number
@app.route('/')
def home():
    student_name = "Yogesh Neupane"
    student_number = "200570557"
    return jsonify({"student_name": student_name, "student_number": student_number})

#webhook fulfillment route
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName', '')
    parameters = req.get('queryResult', {}).get('parameters', {})
    
    if intent == 'FulfillmentIntent':
        #location parameter from user query
        city = parameters.get('geo-city', 'Unknown location')
        
        if city != 'Unknown location':
            # Fetch weather data
            weather_data = fetch_weather(city)
            if weather_data:
                response_text = f"The weather in {city} is {weather_data}."
            else:
                response_text = f"Sorry, I couldn't fetch the weather for {city}."
        else:
            response_text = "Please specify a city to get the weather information."
    else:
        response_text = "Fallback response."

    return jsonify({
        "fulfillmentText": response_text
    })

#function to fetch weather data
def fetch_weather(city):
    try:
        response = requests.get(WEATHER_URL, params={
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        })
        data = response.json()
        if response.status_code == 200:
            # Extract and format weather details
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            return f"{temp}°C with {description}"
        else:
            return None
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

if __name__ == '__main__':
    app.run(debug=True)
