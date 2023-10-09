import requests
import json

# Definiendo el endpoint de la API
api_url = "https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/devops"

# Definiendo los datos a enviar en formato JSON
data = {
    "name": "Victor Villar",
    "mail": "victor.villar@globant.com",
    "github_url": "https://github.com/VVillar/tu-latam-challenge.git"
}

# Enviando el request con el metodo POST
try:
    response = requests.post(api_url, json=data)

    # Revisando el status code de la respuesta
    if response.status_code == 200:
        print("POST request exitoso")
    else:
        print(f"POST request falló con el código de error {response.status_code}")
except Exception as e:
    print(f"Ocurrio un error: {str(e)}")