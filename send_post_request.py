import requests
import json

def send_post_request(api_url, data):
    try:
        response = requests.post(api_url, json=data)

        if response.status_code == 200:
            return True, response.json()
        else:
            return False, f"El post request falló con el código de error {response.status_code}"
    except Exception as e:
        return False, f"Ocurrio un error: {str(e)}"

if __name__ == "__main__":
    api_url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/devops"
    data = {
        "name": "Victor Villar",
        "mail": "victor.villar@globant.com",
        "github_url": "https://github.com/VVillar/tu-latam-challenge.git"
    }

    success, response_data = send_post_request(api_url, data)

    if success:
        print("Success")
        print(json.dumps(response_data, indent=4))
    else:
        print(response_data)
