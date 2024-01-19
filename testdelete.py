import requests

# Define la URL de tu API local
base_url = "http://192.168.56.215:40009/"  # Ajusta el puerto según tu configuración

# Endpoint para eliminar usuarios
delete_user_endpoint = "/users"

# ID del usuario que deseas eliminar (reemplaza con el ID real)
user_id_to_delete = 2

# Construye la URL completa
url = base_url + delete_user_endpoint + f"/{user_id_to_delete}"

# Realiza la solicitud DELETE para eliminar el usuario
response = requests.delete(url)

# Verifica el código de estado
if response.status_code == 200:
    print("Usuario eliminado correctamente")
    print(response.json())  # Si la respuesta incluye datos, imprímelos
else:
    print(f"Error al eliminar usuario. Código de estado: {response.status_code}")
    print("Detalles de la respuesta:", response.text)
