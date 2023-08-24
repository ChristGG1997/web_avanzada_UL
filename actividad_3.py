# dado dos diccionarios primero de productos y segundo de categoria, 
# conocer tercero que permita tener el nombre de su producto y su categoria 

# Diccionarios de productos y categorías
productos = [
    {'id': 1, 'nombre': 'manzana', 'precio': 12000, 'id_categoria': 1},
    {'id': 2, 'nombre': 'leche', 'precio': 3500, 'id_categoria': 2},
    # Agrega más productos aquí si es necesario
]

categorias = {
    1: 'fruta',
    2: 'lácteo',
    # Agrega más categorías aquí si es necesario
}

# Crear un diccionario combinado con nombre del producto y categoría
productos_con_categorias = {}

for producto in productos:
    producto_id = producto['id']
    nombre_producto = producto['nombre']
    id_categoria = producto['id_categoria']
    nombre_categoria = categorias.get(id_categoria, 'Categoría desconocida')
    
    productos_con_categorias[nombre_producto] = nombre_categoria

# Imprimir el diccionario resultante
for producto, categoria in productos_con_categorias.items():
    print(f"Producto: {producto} - Categoría: {categoria}")

