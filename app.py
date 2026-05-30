from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv

from db import get_connection
from validators import validar_cita
from email_service import enviar_confirmacion_cita

load_dotenv()

app = Flask(__name__)
CORS(app)


# -------------------------
# RUTA PRINCIPAL
# -------------------------
@app.route("/")
def inicio():
    return jsonify({
        "mensaje": "Backend Flask activo",
        "proyecto": "Dra. Conchita Campaña - Clínica Dental"
    })


# -------------------------
# OBTENER CITAS
# -------------------------
@app.route("/citas", methods=["GET"])
def obtener_citas():

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM citas")
    citas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(citas)


# -------------------------
# CREAR CITA
# -------------------------
@app.route("/citas", methods=["POST"])
def crear_cita():

    try:
        data = request.json
        print("DATA RECIBIDA:", data)

        errores = validar_cita(data)

        if errores:
            return jsonify({"errores": errores}), 400

        conexion = get_connection()
        cursor = conexion.cursor()

        sql = """
        INSERT INTO citas(
            nombre_paciente,
            telefono,
            correo,
            fecha,
            hora,
            servicio
        )
        VALUES(%s, %s, %s, %s, %s, %s)
        """

        valores = (
            data["nombre"],
            data["telefono"],
            data["correo"],
            data["fecha"],
            data["hora"],
            data["servicio"]
        )

        cursor.execute(sql, valores)
        conexion.commit()

        cursor.close()
        conexion.close()

        enviar_confirmacion_cita(
            data["nombre"],
            data["correo"],
            data["fecha"],
            data["hora"]
        )

        return jsonify({
            "mensaje": "Cita registrada correctamente"
        }), 201

    except Exception as e:
        print("ERROR EN /CITAS:", str(e))
        return jsonify({
            "error": "Error interno del servidor",
            "detalle": str(e)
        }), 500


# -------------------------
# RUN LOCAL
# -------------------------
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
