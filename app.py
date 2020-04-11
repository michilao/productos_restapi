from flask import Flask, jsonify, request

app = Flask (__name__)

from productos import productos

@app.route('/f5')
def ping():
    return jsonify ({"message": "ALLOK" }) #devuelve el string en forma de objeto (jsonify)

@app.route ('/productos', methods = ['GET']) 
def getProductos():
    return jsonify ({"productos": productos})

@app.route ('/productos/<string:producto_name>')
def getProducto(producto_name):
    print (producto_name)
    ProductosFound = [producto for producto in productos if producto['name'] == producto_name]
    if (len(ProductosFound)> 0):
        return jsonify ({"producto" : ProductosFound[0]})
    return jsonify ({"message": "producto no registrado"})

@app.route ('/productos', methods = ['POST'])
def addProducts():
    nuevo_producto = {
    "name": request.json['name'],
    "price": request.json ['price'],
    "cantidad": request.json ['cantidad']
    }
    productos.append(nuevo_producto)
    return jsonify ({"mensaje": "el producto fue agregado", "productos": productos})

@app.route('/productos/<string:producto_name>', methods = ['PUT'])
def editarProducto(producto_name):
    productFound =[producto for producto in productos if producto['name'] == producto_name]
    if (len(productFound)> 0):
        productFound[0]['name'] = request.json ['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['cantidad'] = request.json['cantidad']
        return jsonify({
            "mensaje": "producto editado",
            "producto": productFound[0]
        })
    return jsonify ({"mensaje": "no se encontro producto"})

@app.route ('/productos/<string:producto_name>', methods = ['DELETE'])
def borrarProducto(producto_name):
    ProductosFound =[producto for producto in productos if producto['name'] == producto_name]
    if len(ProductosFound) > 0:
        productos.remove(ProductosFound[0])
        return jsonify ({
            "mensaje": "Producto eliminado",
            "prodfuctos": productos
        })
    return jsonify({"mensaje": "producto no encontrado"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)

