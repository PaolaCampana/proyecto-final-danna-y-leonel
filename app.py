from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

app = Flask(__name__)
CORS(app, origins="*")


# -----------------------
# CONEXIÓN BD
# -----------------------
def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        ssl_disabled=False
    )


# -----------------------
# HOME
# -----------------------
@app.route("/")
def home():
    return jsonify({
        "mensaje": "Backend Flask activo",
        "proyecto": "Clínica Dental"
    })


# -----------------------
# GET CITAS
# -----------------------
@app.route("/citas", methods=["GET"])
def get_citas():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM citas")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(data)


# -----------------------
# POST CITAS
# -----------------------
@app.route("/citas", methods=["POST"])
def add_cita():
    data = request.json

    conn = get_connection()
    cursor = conn.cursor()

    sql = """
    INSERT INTO citas (
        nombre_paciente,
        telefono,
        correo,
        fecha,
        hora,
        servicio
    ) VALUES (%s,%s,%s,%s,%s,%s)
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
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"mensaje": "Cita creada"}), 201


# -----------------------
# RUN
# -----------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
