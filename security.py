from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)


def generar_hash(password):

    return generate_password_hash(password)


def verificar_password(password_plano, password_hash):

    return check_password_hash(
        password_hash,
        password_plano
    )