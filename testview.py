import requests

# Define la URL de tu API local
base_url = "http://192.168.1.24:40009/"  # Ajusta el puerto según tu configuración

# Endpoint para ver todos los usuarios
view_users_endpoint = "/users/view"

# Construye la URL completa
url = base_url + view_users_endpoint

# Realiza la solicitud GET para obtener todos los usuarios
response = requests.get(url)

# Verifica el código de estado antes de intentar leer el JSON
if response.status_code == 200:
    users_data = response.json().get('users', [])
    
    if users_data:
        print("Usuarios registrados:")
        for user in users_data:
            print(f"ID: {user['id_users']}, Nombre: {user['name_users']}, Apellido Paterno: {user['app_users']}")
    else:
        print("No hay usuarios registrados.")
else:
    print(f"Error al obtener usuarios. Código de estado: {response.status_code}")
    print("Detalles de la respuesta:", response.text)
