import requests

print(
    requests.post(
        "http://127.0.0.1:10000",
        json={
            "query": "Who won cricket world cup at 2007?"
        }
    ).json()
)
