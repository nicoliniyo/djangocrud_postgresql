import requests
import json
import os

# Replace with your actual API key
AWANLLM_API_KEY = os.getenv('AWANLLM_API_KEY')


# @app.route("/ask", methods=["POST"])
# def handle_request():
#     user_input = request.form["user_input"]
#     if user_input:
#         response = send_request(user_input)
#         api_response = process_response(response)
#         return json.dumps({"response": api_response})
#     else:
#         return json.dumps({"error": "Please enter some text"})

def send_request(user_input):
    url = "https://api.awanllm.com/v1/chat/completions"

    payload = json.dumps({
        "model": "Meta-Llama-3-8B-Instruct",
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {AWANLLM_API_KEY}"
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print('RESPONSE: ')
    print(response.json())
    content = response.json().get("choices")[0].get("message").get("content")
    print('CONTENT: ')
    print(content)

    return content
    # return response.json()
    # return response.json().get("choices")[0].get("message").get("content")


# def process_response(response):
#     # Extract the API response from the JSON
#     api_response = response.get("choices")[0].get("content")
#     return api_response

def get_content_from_json(json_data):
    # Parse the JSON data into a Python dictionary
    data = json.loads(json_data)

    # Get the 'choices' list
    choices = data['choices']

    # Iterate through the 'choices' list
    for choice in choices:
        # Get the 'message' dictionary
        message = choice['message']

        # Check if the 'content' key exists
        if 'content' in message:
            # Return the 'content' value
            return message['content']

    # If 'content' is not found in any choice, return an empty string
    return ""
