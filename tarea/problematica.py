import sys
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QFormLayout

# Función que se ejecuta cuando se hace clic en "Verificar"
def verificar_inventario():
    nombre_producto = campo_nombre.text()
    cantidad = campo_cantidad.text()
    precio = campo_precio.text()
    
    try:
        # Convertir los campos a los tipos correctos
        cantidad = int(cantidad)
        precio = float(precio)
        
        # Verificar si la cantidad es inferior al mínimo
        if cantidad < 5:
            mensaje = QMessageBox()
            mensaje.setWindowTitle("Advertencia de Stock")
            mensaje.setText(f"El producto '{nombre_producto}' tiene poco stock. Considera reabastecerlo.")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.exec_()
        
        # Calcular el valor total del producto en stock
        valor_total = cantidad * precio
        label_resultado.setText(f"Producto: {nombre_producto}\nCantidad en Stock: {cantidad}\nValor Total: ${valor_total:.2f}")
        
    except ValueError:
        mensaje_error = QMessageBox()
        mensaje_error.setWindowTitle("Error")
        mensaje_error.setText("Asegúrate de que los campos 'Cantidad' y 'Precio' sean numéricos.")
        mensaje_error.setIcon(QMessageBox.Warning)
        mensaje_error.exec_()

# Crear la aplicación
app = QApplication(sys.argv)

# Crear la ventana principal
ventana = QWidget()
ventana.setWindowTitle('Gestión de Inventario')

# Crear un diseño de formulario
form_layout = QFormLayout()

# Crear campos para los datos del producto
campo_nombre = QLineEdit()
campo_cantidad = QLineEdit()
campo_precio = QLineEdit()

# Agregar los campos al formulario con etiquetas
form_layout.addRow('Nombre del Producto:', campo_nombre)
form_layout.addRow('Cantidad en Stock:', campo_cantidad)
form_layout.addRow('Precio Unitario ($):', campo_precio)

# Crear un botón para verificar los datos del inventario
boton_verificar = QPushButton('Verificar')
boton_verificar.clicked.connect(verificar_inventario)
form_layout.addRow(boton_verificar)

# Crear una etiqueta para mostrar el resultado
label_resultado = QLabel('')
form_layout.addRow(label_resultado)

# Asignar el diseño a la ventana
ventana.setLayout(form_layout)

# Ajustar el tamaño de la ventana
ventana.resize(400, 250)

# Mostrar la ventana
ventana.show()

# Iniciar el bucle principal de la aplicación
sys.exit(app.exec_())
