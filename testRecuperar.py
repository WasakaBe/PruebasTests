import requests

# Define la URL de tu API local
base_url = "http://192.168.1.24:40009/"  # Ajusta el puerto según tu configuración

# Endpoint para la recuperación de contraseña
recover_password_endpoint = "/recover-password"

# Datos del usuario para la recuperación de contraseña
recover_user_data = {
    "correo_users": "alexiss@cbta5.net",
}

# Construye la URL completa
recover_password_url = base_url + recover_password_endpoint

# Realiza la solicitud POST para solicitar el token de recuperación
recover_response = requests.post(recover_password_url, json=recover_user_data)

# Verifica el código de estado
if recover_response.status_code == 200:
    print("Token de recuperación de contraseña generado correctamente")
    recovery_token = recover_response.json()['recovery_token']

    # Endpoint para cambiar la contraseña con el token
    change_password_endpoint = "/change-password"

    # Datos para cambiar la contraseña con el token
    change_password_data = {
        "token": recovery_token,
        "new_password": "nueva_contraseña_aqui",
    }

    # Construye la URL completa
    change_password_url = base_url + change_password_endpoint

    # Realiza la solicitud POST para cambiar la contraseña
    change_password_response = requests.post(change_password_url, json=change_password_data)

    # Verifica el código de estado
    if change_password_response.status_code == 200:
        print("Contraseña cambiada correctamente")
    else:
        print(f"Error al cambiar la contraseña. Código de estado: {change_password_response.status_code}")
        print("Detalles de la respuesta:", change_password_response.text)
else:
    print(f"Error al generar token de recuperación. Código de estado: {recover_response.status_code}")
    print("Detalles de la respuesta:", recover_response.text)
