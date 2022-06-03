Característica: Alta de un paciente
    Como administrador del Hospital
    requiero registrar un paciente
    para gestionar su historial y citas médicas.

    Escenario: Datos correctos
        Dado que estoy dentro del sistema
        Y entro a la sección de registro de pacientes
        Y capturo los datos: nombre "María", apellido paterno: "López", apellido materno "Pérez"
        Y el número de seguro social "68456461", fecha de nacimiento "1980-11-21", tipo de sangre "A positivo"
        Y el estado "Zacatecas" del municipio "Gudalupe"
        Cuando presiono el botón Agregar
        Entonces puedo ver el paciente "María López Pérez" en la lista de pacientes registrados.