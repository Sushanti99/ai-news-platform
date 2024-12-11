import json
from summarizer import return_summary
import requests
api_key = "342b2fbe-c269-492d-870d-f85c15c9f2b1"

url = "https://api.exa.ai/search"


def exa_response(query):
    payload = {
      "query": query,
      "useAutoprompt": True,
      "numResults": 10,
      "startPublishedDate": "2023-01-01T00:00:00.000Z",
      "endPublishedDate": "2023-12-31T00:00:00.000Z"
    }

    headers = {
      "x-api-key": api_key,
      "Content-Type": "application/json"
    }

    response = requests.request("POST", url, json=payload, headers=headers)
    response = response.text
    response = json.loads(response)

    url_list = []

    for resp in response["results"]:
        # print(resp["id"])
        url_list.append(resp["id"])

    print(url_list)

    return return_summary(url_list)
