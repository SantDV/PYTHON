class usuario():

    numUsuarios = 0

    def __init__(self, nombre, contra):

        self.nombre = nombre
        self.contra = contra
        self.conectado = False
        self.intentos = 3

    def conectar(self):
        miContra = input("Ingrese su contraseña: ")
        if miContra==self.contra:
            print("Se ha conectado con éxito!")
            self.conectado= True
        else:
            print("Contraseña incorrecta, intentelo nuevamente!")
            print("Intentos restantes: ", self.intentos)


    def desconectar(self):
        if self.conectado:
            print("Se cerró la sesón con éxito!")

        else:
            print("Error, sesión no iniciada!")


    def __str__(self):
        if self.conectado:
            connect = "conectado"
        else:
            connect = "Desconectado"

        return f"Nombre de usuario: {self.nombre} \n Estado: {connect}"


user1 = usuario(input("usuario:"), input("Contraseña: "))

user1.conectar()
print(user1)