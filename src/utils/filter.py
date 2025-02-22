import re

def get_api_request(response):
    """
    Extracts the API request string from the model's response and removes any backticks.
    """
    # Try to extract the API request string using regex
    match = re.search(r"(/\w+/\w+\?[^\s`]+)", response)
    if not match:
        return None
    
    # Remove backticks from the extracted string
    api_request = match.group(1).replace("`", "")
    return api_request
    