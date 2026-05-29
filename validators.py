def validar_registro(data):

    errores = []

    if not data:

        errores.append("No se recibieron datos.")
        return errores

    if not data.get("nombre"):

        errores.append("El nombre es obligatorio.")

    if not data.get("categoria"):

        errores.append("La categoría es obligatoria.")

    if not data.get("descripcion"):

        errores.append("La descripción es obligatoria.")

    try:

        precio = float(data.get("precio", 0))

        if precio <= 0:

            errores.append(
                "El precio debe ser mayor que 0."
            )

    except ValueError:

        errores.append(
            "El precio debe ser un número válido."
        )

    return errores


def validar_login(data):

    errores = []

    if not data:

        errores.append(
            "No se recibieron datos."
        )

        return errores

    if not data.get("correo"):

        errores.append(
            "El correo es obligatorio."
        )

    if not data.get("password"):

        errores.append(
            "La contraseña es obligatoria."
        )

    return errores


def validar_contacto(data):

    errores = []

    if not data:

        errores.append(
            "No se recibieron datos."
        )

        return errores

    if not data.get("nombre"):

        errores.append(
            "El nombre es obligatorio."
        )

    if not data.get("correo"):

        errores.append(
            "El correo es obligatorio."
        )

    if not data.get("mensaje"):

        errores.append(
            "El mensaje es obligatorio."
        )

    return errores


def validar_cita(data):

    errores = []

    if not data:

        errores.append(
            "No se recibieron datos."
        )

        return errores

    if not data.get("nombre"):

        errores.append(
            "Nombre obligatorio."
        )

    if not data.get("telefono"):

        errores.append(
            "Teléfono obligatorio."
        )

    if not data.get("fecha"):

        errores.append(
            "Fecha obligatoria."
        )

    if not data.get("hora"):

        errores.append(
            "Hora obligatoria."
        )

    return errores