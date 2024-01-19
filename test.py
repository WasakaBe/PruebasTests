import requests

# Define la URL de tu API local
base_url = "http://192.168.56.215:40009/"  # Ajusta el puerto según tu configuración

# Endpoint para la inserción de usuarios
insert_user_endpoint = "/users/insert"

# Datos del nuevo usuario que deseas insertar
new_user_data = {
    "name_users": "carlos",
    "app_users": "cifuente",
    "correo_users": "carlos@cifuentes.net",
    "pwd_users": "carloscifuentes123",
    "idRol": 3,
    "idSexo": 2,
    "idParental": 3,
    "no_control_users": 888836389012345
}

# Construye la URL completa
url = base_url + insert_user_endpoint

# Realiza la solicitud POST para insertar el nuevo usuario
response = requests.post(url, json=new_user_data)

# Verifica el código de estado
if response.status_code == 201:
    print("Usuario insertado correctamente")
    print(response.json())  # Si la respuesta incluye datos, imprímelos
else:
    print(f"Error al insertar usuario. Código de estado: {response.status_code}")
    print("Detalles de la respuesta:", response.text)
