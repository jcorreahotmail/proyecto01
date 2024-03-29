import requests

def obtener_direccion_ip_publica():
    try:
        # Hacer una solicitud a un servicio que devuelva la dirección IP pública
        respuesta = requests.get('https://api.ipify.org')
        # Extraer la dirección IP de la respuesta
        direccion_ip = respuesta.text
        return direccion_ip
    except Exception as e:
        print("Error al obtener la dirección IP pública:", e)
        return None

# Ejemplo de uso
direccion_ip_publica = obtener_direccion_ip_publica()
if direccion_ip_publica:
    print("La dirección IP pública es:", direccion_ip_publica)
else:
    print("No se pudo obtener la dirección IP pública.")
