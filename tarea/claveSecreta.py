import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

# Función que se ejecuta cuando el botón es presionado
def mostrar_clave():
    clave = campo_clave.text()
    label_resultado.setText(f"La clave ingresada es: {clave}")

# Crear la aplicación
app = QApplication(sys.argv)

# Crear la ventana principal
ventana = QWidget()
ventana.setWindowTitle('Ingreso de Clave Secreta')

# Crear un diseño vertical
layout = QVBoxLayout()

# Crear etiqueta de instrucción
label_instruccion = QLabel('Por favor, ingresa tu clave secreta:')
layout.addWidget(label_instruccion)

# Crear el campo de entrada de clave
campo_clave = QLineEdit()
campo_clave.setEchoMode(QLineEdit.Password)  # Establecer modo de entrada de contraseña
layout.addWidget(campo_clave)

#  botón para enviar la clave
boton_enviar = QPushButton('Enviar')
boton_enviar.clicked.connect(mostrar_clave)
layout.addWidget(boton_enviar)

#  etiqueta para mostrar el resultado
label_resultado = QLabel('')
layout.addWidget(label_resultado)

# diseño a la ventana
ventana.setLayout(layout)

#  tamaño de la ventana
ventana.resize(300, 150)

# Mostrar la ventana
ventana.show()

# Iniciar el bucle principal de la aplicación
sys.exit(app.exec_()) 