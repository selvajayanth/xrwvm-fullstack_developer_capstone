# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

# def get_request(endpoint, **kwargs):
import requests

def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"
    
    request_url = backend_url + endpoint + "?" + params.rstrip("&")  # Remove trailing '&'
    
    print(f"GET from {request_url}")
    
    try:
        response = requests.get(request_url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Print HTTP error
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")  # Print connection error
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")  # Print timeout error
    except requests.exceptions.RequestException as req_err:
        print(f"Request exception occurred: {req_err}")  # Print any other request error
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Print unexpected error
    
    return None  # Return None if there was an error

# def analyze_review_sentiments(text):
# request_url = sentiment_analyzer_url+"analyze/"+text
def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")
# def post_review(data_dict):
def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
# Add code for posting review
