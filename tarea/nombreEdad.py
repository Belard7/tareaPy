import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

# Crear una aplicación
app = QApplication(sys.argv)

# Crear una ventana principal
ventana = QWidget()
ventana.setWindowTitle('Mi Información')

# Crear un diseño vertical
layout = QVBoxLayout()

# Crear etiquetas para el nombre y la edad
nombre_completo = QLabel('Jimmy Rivas')
edad = QLabel('27 años')

### Aplicar formato de alineación al centro
nombre_completo.setAlignment(Qt.AlignCenter)
edad.setAlignment(Qt.AlignCenter)

# Cambiar el tamaño de la fuente de las etiquetas
nombre_completo.setStyleSheet("font-size: 20px;")
edad.setStyleSheet("font-size: 20px;")

# Añadir las etiquetas al diseño
layout.addWidget(nombre_completo)
layout.addWidget(edad)

# Asignar el diseño a la ventana
ventana.setLayout(layout)

# Ajustar el tamaño de la ventana y centrarla
ventana.resize(400, 200)
ventana.move((app.desktop().screenGeometry().width() - ventana.width()) // 2, 
             (app.desktop().screenGeometry().height() - ventana.height()) // 2)

# Mostrar la ventana
ventana.show()

# Iniciar el bucle de la aplicación
sys.exit(app.exec_())
