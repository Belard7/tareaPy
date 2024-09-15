import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QFormLayout

# Función que se ejecuta cuando el botón es presionado
def enviar_datos():
    # Obtener los datos ingresados de los campos
    datos = {
        "Nombre": campo_nombre.text(),
        "Edad": campo_edad.text(),
        "Dirección": campo_direccion.text(),
        "Teléfono": campo_telefono.text(),
        "Correo Electrónico": campo_email.text(),
        "Ocupación": campo_ocupacion.text(),
        "Estado Civil": campo_estado_civil.text(),
        "Nacionalidad": campo_nacionalidad.text(),
        "Documento de Identidad": campo_documento.text(),
        "Fecha de Nacimiento": campo_fecha_nacimiento.text(),
    }

    # Verificar si hay algún campo vacío
    campos_vacios = [campo for campo, valor in datos.items() if not valor.strip()]
    if campos_vacios:
        # Mostrar un mensaje de advertencia si hay campos vacíos
        mensaje_error = QMessageBox()
        mensaje_error.setWindowTitle("Error")
        mensaje_error.setText(f"Los siguientes campos están vacíos: {', '.join(campos_vacios)}")
        mensaje_error.setIcon(QMessageBox.Warning)
        mensaje_error.exec_()
    else:
        # Mostrar los datos ingresados en un cuadro de mensaje
        mensaje_exito = QMessageBox()
        mensaje_exito.setWindowTitle("Datos Ingresados")
        mensaje_exito.setText("\n".join([f"{campo}: {valor}" for campo, valor in datos.items()]))
        mensaje_exito.setIcon(QMessageBox.Information)
        mensaje_exito.exec_()

# Crear la aplicación
app = QApplication(sys.argv)

# Crear la ventana principal
ventana = QWidget()
ventana.setWindowTitle('Ingreso de Datos Personales')

# Crear un diseño de formulario
form_layout = QFormLayout()

# Crear campos para los 10 datos característicos de la persona
campo_nombre = QLineEdit()
campo_edad = QLineEdit()
campo_direccion = QLineEdit()
campo_telefono = QLineEdit()
campo_email = QLineEdit()
campo_ocupacion = QLineEdit()
campo_estado_civil = QLineEdit()
campo_nacionalidad = QLineEdit()
campo_documento = QLineEdit()
campo_fecha_nacimiento = QLineEdit()

# Agregar los campos al formulario con etiquetas
form_layout.addRow('Nombre Completo:', campo_nombre)
form_layout.addRow('Edad:', campo_edad)
form_layout.addRow('Dirección:', campo_direccion)
form_layout.addRow('Teléfono:', campo_telefono)
form_layout.addRow('Correo Electrónico:', campo_email)
form_layout.addRow('Ocupación:', campo_ocupacion)
form_layout.addRow('Estado Civil:', campo_estado_civil)
form_layout.addRow('Nacionalidad:', campo_nacionalidad)
form_layout.addRow('Documento de Identidad:', campo_documento)
form_layout.addRow('Fecha de Nacimiento:', campo_fecha_nacimiento)

# Crear un botón para enviar los datos
boton_enviar = QPushButton('Enviar')
boton_enviar.clicked.connect(enviar_datos)  # Conectar el botón a la función enviar_datos
form_layout.addRow(boton_enviar)

# Asignar el diseño a la ventana
ventana.setLayout(form_layout)

# Ajustar el tamaño de la ventana
ventana.resize(400, 400)

# Mostrar la ventana
ventana.show()

# Iniciar el bucle principal de la aplicación
sys.exit(app.exec_())
