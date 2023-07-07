import requests
import json

def send_chat_request(user_input, history):
    url = "http://localhost:5000/api/v1/chat"  # Replace with the appropriate API endpoint
    headers = {'Content-Type': 'application/json'}

    payload = {
        'user_input': user_input,
        'history': history,
        'charcter_id': 'Gabriel',
        'instruction_template': 'Vicuna-v1.1',
    }

    print(json.dumps(payload))

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raise an exception if the request was not successful

        print(str(response.json()['results'][0]['history']['visible']))
        print(response.json()['results'][0]['history']['visible'][-1][1])

    except requests.exceptions.RequestException as e:
        error_code = response.status_code
        error_message = response.text
        print(f"Error: {error_code} - {error_message}")

# Example usage
user_input = "Me, nothing - what do you know about Herzog?"
history = {'visible':[],'internal':[]}
history['visible'].append("How are you?")
history['visible'].append("What do You know about the shoe that Werner Herzog ate?")
history['internal'].append("How are you?")
history['internal'].append("What do You know about the shoe that Werner Herzog ate?")

send_chat_request(user_input, history)

