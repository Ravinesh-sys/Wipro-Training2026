import requests
import json

def fetch_users():
    
    url = "https://jsonplaceholder.typicode.com/users"

    # Custom headers
    headers = {
        "User-Agent": "Python-Requests-Client",
        "Accept": "application/json"
    }

    try:
        # Sending GET request with headers
        response = requests.get(url, headers=headers)

        # Raise exception for HTTP errors (4xx, 5xx)
        response.raise_for_status()

        # Parse JSON response
        users_data = response.json()

        # Extract required fields
        extracted_users = []
        for user in users_data:
            extracted_users.append({
                "id": user.get("id"),
                "name": user.get("name"),
                "email": user.get("email"),
                "city": user.get("address", {}).get("city")
            })

        # Save extracted data into a JSON file
        with open("users_data.json", "w") as file:
            json.dump(extracted_users, file, indent=4)

        print("Data successfully fetched and saved to users_data.json")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API")

    except requests.exceptions.Timeout:
        print("Error: The request timed out")

    except requests.exceptions.RequestException as err:
        print(f"Unexpected error occurred: {err}")

    except Exception as e:
        print(f"General error: {e}")


# Function call
fetch_users()
