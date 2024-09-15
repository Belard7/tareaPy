import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout

# Función que se ejecuta cuando el botón es presionado
def enviar_datos():
    nombre = campo_nombre.text()
    cedula = campo_cedula.text()
    label_resultado.setText(f"Nombre: {nombre}\nCédula: {cedula}")

# Crear la aplicación
app = QApplication(sys.argv)

#  ventana principal
ventana = QWidget()
ventana.setWindowTitle('Ingreso de Datos')

#  diseño vertical
layout = QVBoxLayout()

#  etiqueta y campo de entrada para el nombre completo
label_nombre = QLabel('Nombre Completo:')
campo_nombre = QLineEdit()
layout.addWidget(label_nombre)
layout.addWidget(campo_nombre)

#  etiqueta y campo de entrada para el número de cédula
label_cedula = QLabel('Número de Cédula:')
campo_cedula = QLineEdit()
layout.addWidget(label_cedula)
layout.addWidget(campo_cedula)

#  botón para enviar los datos
boton_enviar = QPushButton('Enviar')
boton_enviar.clicked.connect(enviar_datos)  # Conectar el botón a la función enviar_datos
layout.addWidget(boton_enviar)

# etiqueta para mostrar el resultado
label_resultado = QLabel('')
layout.addWidget(label_resultado)

# diseño a la ventana
ventana.setLayout(layout)

# amaño de la ventana
ventana.resize(300, 200)

# Mostrar la ventana
ventana.show()

# Iniciar el bucle principal de la aplicación
sys.exit(app.exec_())
