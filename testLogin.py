import requests

# Define la URL de tu API local
base_url = "http://192.168.56.215:40009/"  # Ajusta el puerto según tu configuración

# Endpoint para el proceso de inicio de sesión
login_endpoint = "/login"

# Datos de inicio de sesión
login_data = {
    "correo_users": "juan@gmail.com",  # Ajusta con un correo de prueba válido
    "pwd_users": "alumnopass1"  # Ajusta con una contraseña de prueba válida
}

# Construye la URL completa
url = base_url + login_endpoint

# Realiza la solicitud POST para el inicio de sesión
response = requests.post(url, json=login_data)

# Verifica el código de estado antes de intentar leer el JSON
if response.status_code == 200:
    print("Inicio de sesión exitoso")
    print(response.json())  # Si la respuesta incluye datos, imprímelos
else:
    print(f"Error en el inicio de sesión. Código de estado: {response.status_code}")
    print("Detalles de la respuesta:", response.text)
