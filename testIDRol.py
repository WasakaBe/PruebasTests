import requests

# Define la URL de tu API local
base_url = "http://192.168.1.24:40009/"  # Ajusta el puerto según tu configuración

# ID del rol de usuario que deseas obtener
rol_user_id = 1  # Ajusta este valor según tu caso

# Endpoint para obtener un rol de usuario por ID
get_rol_user_endpoint = f"rols_user/{rol_user_id}"

# Construye la URL completa
url = base_url + get_rol_user_endpoint

# Realiza la solicitud GET para obtener el rol de usuario por ID
response = requests.get(url)

# Verifica el código de estado antes de intentar leer el JSON
if response.status_code == 200:
    print("Rol de usuario obtenido correctamente")
    print(response.json())  # Si la respuesta incluye datos, imprímelos
else:
    print(f"Error al obtener rol de usuario. Código de estado: {response.status_code}")
    print("Detalles de la respuesta:", response.text)
