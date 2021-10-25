class Email:

    def __init__(self, destinatario, asunto, contenido, estado):
        self.destinatario = destinatario
        self.asunto = asunto
        self.contenido = contenido
        self.estado = estado

Email1 = Email("mariopisquiy@ufm.edu","Correo de prueba","Hola! te saludo desde mi nuevo correo","Enviado")
print(f"Correo Electrónico 1: \n Destinatario: {Email1.destinatario} \n Asunto: {Email1.asunto} \n Cuerpo: {Email1.contenido} \n Estado: {Email1.estado}")