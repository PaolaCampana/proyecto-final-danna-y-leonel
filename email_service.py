import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def enviar_confirmacion_cita(nombre, correo, fecha, hora):

    try:
        print("Intentando enviar correo...")
        print("Correo destino:", correo)

        email = EmailMessage()
        email["Subject"] = "Confirmación de cita dental"
        email["From"] = os.getenv("MAIL_USER")
        email["To"] = correo

        email.set_content(f"""
Hola {nombre}

Tu cita fue registrada correctamente.

Fecha: {fecha}
Hora: {hora}

Gracias por confiar en nosotros.
Dra. Conchita Campaña
""")

        servidor = os.getenv("MAIL_SERVER")
        puerto = int(os.getenv("MAIL_PORT"))
        usuario = os.getenv("MAIL_USER")
        password = os.getenv("MAIL_PASSWORD")

        print("Conectando con SMTP...")
        print("Servidor:", servidor)
        print("Puerto:", puerto)
        print("Usuario:", usuario)

        with smtplib.SMTP(servidor, puerto) as smtp:
            smtp.set_debuglevel(1)

            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()

            print("Iniciando sesión...")
            smtp.login(usuario, password)

            print("Enviando mensaje...")
            smtp.send_message(email)

        print("Correo enviado correctamente")

    except Exception as e:
        print("ERROR CORREO COMPLETO:")
        print(repr(e))