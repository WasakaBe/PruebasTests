import requests

# Define la URL de tu API local
base_url = "http://192.168.1.24:40009/"  # Ajusta el puerto según tu configuración

# Endpoint para obtener todos los roles de usuario
get_all_rols_user_endpoint = "/rols_user/view"

# Construye la URL completa
url = base_url + get_all_rols_user_endpoint

# Realiza la solicitud GET para obtener todos los roles de usuario
response = requests.get(url)

# Verifica el código de estado antes de intentar leer el JSON
if response.status_code == 200:
    # Si la respuesta incluye datos, imprímelos
    roles_user_data = response.json()
    print("Roles de usuario:")
    for role_user in roles_user_data['rols_user']:
        print(f"ID: {role_user['id_rols_user']}, Nombre: {role_user['name_rols_user']}")
else:
    print(f"Error al obtener roles de usuario. Código de estado: {response.status_code}")
    print("Detalles de la respuesta:", response.text)
