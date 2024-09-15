import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFormLayout

# Función que se ejecuta cuando el botón es presionado
def enviar_datos():
    # Obtener los datos ingresados para cada mascota
    mascota1 = f"Mascota 1: Nombre: {campo_nombre1.text()}, Edad: {campo_edad1.text()}, Tipo: {campo_tipo1.text()}"
    mascota2 = f"Mascota 2: Nombre: {campo_nombre2.text()}, Edad: {campo_edad2.text()}, Tipo: {campo_tipo2.text()}"
    mascota3 = f"Mascota 3: Nombre: {campo_nombre3.text()}, Edad: {campo_edad3.text()}, Tipo: {campo_tipo3.text()}"

    # Mostrar los datos ingresados en la etiqueta de resultado
    label_resultado.setText(f"{mascota1}\n{mascota2}\n{mascota3}")

# Crear la aplicación
app = QApplication(sys.argv)

# Crear la ventana principal
ventana = QWidget()
ventana.setWindowTitle('Ingreso de Datos de Mascotas')

# Crear un diseño de formulario
form_layout = QFormLayout()

# Crear campos para la mascota 1
label_mascota1 = QLabel('Mascota 1')
campo_nombre1 = QLineEdit()
campo_edad1 = QLineEdit()
campo_tipo1 = QLineEdit()
form_layout.addRow(label_mascota1)
form_layout.addRow('Nombre:', campo_nombre1)
form_layout.addRow('Edad:', campo_edad1)
form_layout.addRow('Tipo:', campo_tipo1)

# Crear campos para la mascota 2
label_mascota2 = QLabel('Mascota 2')
campo_nombre2 = QLineEdit()
campo_edad2 = QLineEdit()
campo_tipo2 = QLineEdit()
form_layout.addRow(label_mascota2)
form_layout.addRow('Nombre:', campo_nombre2)
form_layout.addRow('Edad:', campo_edad2)
form_layout.addRow('Tipo:', campo_tipo2)

# Crear campos para la mascota 3
label_mascota3 = QLabel('Mascota 3')
campo_nombre3 = QLineEdit()
campo_edad3 = QLineEdit()
campo_tipo3 = QLineEdit()
form_layout.addRow(label_mascota3)
form_layout.addRow('Nombre:', campo_nombre3)
form_layout.addRow('Edad:', campo_edad3)
form_layout.addRow('Tipo:', campo_tipo3)

# Crear un botón para enviar los datos
boton_enviar = QPushButton('Enviar')
boton_enviar.clicked.connect(enviar_datos)  # Conectar el botón a la función enviar_datos
form_layout.addRow(boton_enviar)

# Crear una etiqueta para mostrar el resultado
label_resultado = QLabel('')
form_layout.addRow(label_resultado)

# Asignar el diseño a la ventana
ventana.setLayout(form_layout)

# Ajustar el tamaño de la ventana
ventana.resize(400, 300)

# Mostrar la ventana
ventana.show()

# Iniciar el bucle principal de la aplicación
sys.exit(app.exec_())
