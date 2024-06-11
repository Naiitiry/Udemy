import os
import pandas as pd

class Inventario:
    
    # Buscamos el archivo .csv con el módulo "os"

    ruta_archivo = os.path.join(os.path.dirname(__file__),'data','detalle_productos.csv')

    @classmethod
    def verificar_archivo(cls):
        # Verificar si el directorio existe, si no, crearlo
        if not os.path.exists(os.path.dirname(cls.ruta_archivo)):
            os.makedirs(os.path.dirname(cls.ruta_archivo))

    @classmethod
    def agregar_producto(cls,producto):
        cls.verificar_archivo()
        # Crear un DataFrame temporal con el nuevo producto
        nuevo_producto = pd.DataFrame([{
            'Categoria':producto.categoria,
            'Marca': producto.marca,
            'Nombre':producto.nombre,
            'Precio':producto.precio,
            'Cantidad':producto.cantidad,
            'Peso':producto.peso
        }])
        # Cargar el DataFrame existente y agregar el nuevo producto
        df=pd.read_csv(cls.ruta_archivo)
        # Eliminamos las filas vacías de Dataframes cada vez que creamos un archivo nuevo.
        df=pd.concat([df.dropna(how='all'),nuevo_producto],ignore_index=False)
        # Guardar los cambios en el archivo .csv
        df.to_csv(cls.ruta_archivo,index=False)

    @classmethod
    def listar_producto(cls):
        cls.verificar_archivo()
        df = pd.read_csv(cls.ruta_archivo)
        return df
    
    @classmethod
    def buscar_producto(cls,categoria):
        cls.verificar_archivo()
        df=pd.read_csv(cls.ruta_archivo)
        resultado = df[df['Categoria']==categoria]
        return resultado

    @classmethod
    def modificar_producto(cls,categoria,marca,nombre,nuevo_precio=None,nuevo_peso=None,nuevo_cantidad=None):
        cls.verificar_archivo()
        df=pd.read_csv(cls.ruta_archivo)

        # Buscar el índice del producto a modificar
        condicion = (df['Categoria']== categoria) & (df['Marca']==marca) & (df['Nombre']==nombre)
        indices= df.index[condicion]

        if not indices.empty:
            index=indices[0] # Asumiendo que hay una combinación única de nombre, categoría y marca
            if nuevo_peso is not None:
                df.at[index,'Peso'] = nuevo_peso
            if nuevo_precio is not None:
                df.at[index,'Precio'] = nuevo_precio
            if nuevo_cantidad is not None:
                df.at[index,'Cantidad'] = nuevo_cantidad
            # Guardar el DataFrame modificado de vuelta al archivo .csv
            df.to_csv(cls.ruta_archivo,index=False)
            print(f'Producto {nombre} modificado con éxito.')
        else:
            print(f'Producto {nombre} no encontrado.')

    @classmethod
    def eliminar_producto(cls,categoria,marca,nombre):
        cls.verificar_archivo()
        df=pd.read_csv(cls.ruta_archivo)
        condicion = (df['Categoria']== categoria) & (df['Marca']==marca) & (df['Nombre']==nombre)
        indices= df.index[condicion]
        if not indices.empty:
            index=indices[0] # Asumiendo que hay una combinación única de nombre, categoría y marca
            # Eliminar el producto del DataFrame
            df=df.drop(index)
            # Guardar el DataFrame modificado de vuelta al archivo .csv
            df.to_csv(cls.ruta_archivo,index=False)
            print(f'El producto {nombre} fue eliminado exitosamente.')
        else:
            print(f'El producto {nombre} no se encuentra en el archivo.')
