import pandas as pd

# Creación y guardado del archivo .csv
data = {
    'Producto': ['Laptop', 'Teléfono', 'Tablet', 'Monitor'],
    'Precio': [1000, 500, 300, 150],
    'Peso': [2.5, 0.2, 0.5, 3.0],
    'Marca': ['Dell', 'Samsung', 'Apple', 'LG'],
    'Distribuidor': ['Distribuidor A', 'Distribuidor B', 'Distribuidor C', 'Distribuidor D'],
    'Fabricante': ['Fabricante A', 'Fabricante B', 'Fabricante C', 'Fabricante D']
}

df = pd.DataFrame(data)
df.to_csv('productos.csv', index=False)

# Lectura y búsqueda de datos
df = pd.read_csv('productos.csv')

# Buscar información de un producto en particular (por ejemplo, 'Teléfono')
producto_buscado = 'Teléfono'
datos_producto = df[df['Producto'] == producto_buscado]

# Mostrar los datos del producto buscado
print(datos_producto)
