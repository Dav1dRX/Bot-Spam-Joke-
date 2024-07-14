import pyautogui
import webbrowser
from time import sleep
import random

# Supongamos que 'numero.num' contiene el número de teléfono al que deseas enviar el mensaje
numero_telefono = "+34634634672343"

# Lista de mensajes
mensajes = [  """ mensaje 1""",
    """Mensaje 2""",
    """Mensaje 3"""
]

# Corrige la URL
webbrowser.open("https://web.whatsapp.com/send?phone=" + numero_telefono)

# Espera un tiempo suficiente para que se abra la página de WhatsApp Web y cargue completamente
sleep(10)

# Envía los mensajes
for _ in range(500):
    # Selecciona un mensaje aleatorio de la lista
    mensaje = random.choice(mensajes)
    pyautogui.typewrite(mensaje)
    pyautogui.press("enter")
    # Espera un tiempo aleatorio antes de enviar el siguiente mensaje (opcional)
    sleep(random.uniform(1, 3))

