## Challenge DevSecOps/SRE

**send_post_request.py**

El archivo `send_post_request.py` contiene un script en Python que realiza una solicitud POST a una API utilizando la biblioteca `requests`.

En este script:
- Importamos las bibliotecas `requests` y `json` para realizar la solicitud y manejar los datos en formato JSON, respectivamente.
- Definimos una función llamada `send_post_request` que toma dos argumentos: `api_url` y `data`. Esta función realiza la solicitud POST a la URL especificada (`api_url`) con los datos proporcionados (`data`) en formato JSON. Si la solicitud es exitosa, devuelve True y los datos de respuesta; de lo contrario, devuelve False y un mensaje de error.

En la sección `if __name__ == "__main__":`, se configuran valores de ejemplo para la URL de la API (`api_url`) y los datos que se enviarán en la solicitud POST (`data`). Luego, se llama a la función `send_post_request` y se maneja la respuesta de la solicitud.

**test_send_post_request.py**

El archivo `test_send_post_request.py` contiene pruebas unitarias para el script `send_post_request.py` utilizando la biblioteca `unittest`. En este archivo:
- Importamos `unittest` para escribir pruebas unitarias y `patch` para simular las llamadas a la biblioteca `requests` durante las pruebas.
- Definimos una clase llamada `TestSendPostRequest` que hereda de `unittest.TestCase`. Esta clase contiene dos métodos de prueba (`test_send_post_request_success` y `test_send_post_request_failure`) que prueban diferentes escenarios de la función `send_post_request`.
- En el método `test_send_post_request_success`, configuramos un "mock" para simular una respuesta exitosa de la API y probamos si la función `send_post_request` maneja correctamente la respuesta.
- En el método `test_send_post_request_failure`, configuramos el "mock" para lanzar una excepción simulando un error de conexión y probamos si la función maneja correctamente este error.

**api_request_workflow.yml**

El archivo de flujo de GitHub Actions define un proceso automatizado que se ejecuta en respuesta a eventos, como una confirmación de código. En este archivo:
- Configuramos un flujo de GitHub Actions que se activa cuando se realiza una confirmación de código en la rama develop del repositorio.
- El flujo se ejecuta en una máquina virtual con Ubuntu.
- Se realizan varias acciones, incluyendo la comprobación del código, la configuración de la versión de Python, la instalación de las dependencias desde un archivo `requirements.txt`, la ejecución de las pruebas unitarias y, si las pruebas son exitosas (`if: ${{ success() }}`), se realiza una solicitud a la API.
