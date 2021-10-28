from flask import Flask, render_template, request

app= Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home2.html', titulo = 'VipShop Holdings')

@app.route('/admin')
def admin():
    return render_template('admin.html', titulo= 'Dasboard Admin')

@app.route('/products/', methods=['GET', 'POST'])
def anadirProducto():
    if request.method == 'GET':
        return render_template('products.html')
    else:
        pass
        #Registrar nuevo producto en la BD y mostrarlo en la vista productos

@app.route('/products/calificar', methods=['GET', 'POST'])
def comentar():
    if request.method == 'GET':
        return render_template('calificar.html')
    else:
        pass
        #guardar comentario en la base de datos

@app.route('/admin/anadirproductos', methods=['GET', 'POST'])
def anadirproducto():
    if request.method == 'GET':
        return render_template('anadirProducto.html')
    else:
        pass
        #Registrar nuevo producto en la BD y mostrarlo en la vista productos

@app.route('/admin/deleteproduct', methods=['GET', 'POST'])
def eliminarproducto():
    if request.method == 'GET':
        return render_template('deleteProduct.html')
    else:
        pass
        #Eliminar producto en la BD y retornar a pagina de elminación.

if __name__ == '__main__':
    app.run(debug=True)
