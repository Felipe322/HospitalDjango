Característica: Login del sistema
    Como usuario
    requiero iniciar sesión en el sistema de Hospital
    para realizar mis acitividades como administrador.

    Escenario: Credenciales válidas
        Dado que ingreso el usuario "alex@asdas.mx" 
        Y la contraseña "alex123"
        Cuando presiono el botón Ingresar
        Entonces puedo ver en la página principal el nombre de mi usuario "alex@asdas.mx"