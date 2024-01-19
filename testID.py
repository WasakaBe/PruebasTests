import requests

# Define la URL de tu API local
base_url = "http://192.168.56.215:40009/"  # Ajusta el puerto según tu configuración

# Endpoint para obtener un usuario por ID
get_user_by_id_endpoint = "/users/2"  # Cambia el ID según el usuario que quieras obtener

# Construye la URL completa
url = base_url + get_user_by_id_endpoint

# Realiza la solicitud GET para obtener el usuario por ID
response = requests.get(url)

# Verifica el código de estado
if response.status_code == 200:
    print("Usuario obtenido correctamente")
    print(response.json())  # Si la respuesta incluye datos, imprímelos
else:
    print(f"Error al obtener usuario. Código de estado: {response.status_code}")
    print("Detalles de la respuesta:", response.text)
