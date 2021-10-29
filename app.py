from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import redirect
from db import seleccion, accion
from datetime import datetime
app= Flask(__name__)

app.secret_key = 'secret'

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
        return render_template('products.html', titulo= 'Tienda | VipShop')
    else:
        pass
        #Registrar nuevo producto en la BD y mostrarlo en la vista productos
@app.route('/products/calificar', methods=['GET', 'POST'])
def comentar():
    if request.method == 'GET':
        sql1 = 'SELECT codigo, nombre, descripcion, precio, imagen FROM tblProducto'
        res1= seleccion(sql1)
        print(len(res1))
        dic_comments = {}
        for prod in res1:
            codprod= prod[0]
            sql2 = f"SELECT nombreUsuario, codigoProducto, calificacion, comentario, fecha FROM tblComentarios WHERE codigoProducto='{codprod}'"
            res2= seleccion(sql2)
            if len(res2)>0:
                res5=[]
                for i in range(len(res2)):
                    sql3= f"SELECT imagen FROM tblUsuarios WHERE usuario='{res2[i][0]}'"
                    res3=seleccion(sql3)
                    res4= res2[i]+res3[0]
                    res5.append(res4)
                    dic_comments[codprod]=res5
        return render_template('calificar-todos.html',titulo= 'Productos | VipShop', username = 'jperez', products= res1, comments= dic_comments, i=1)
        
    else:
        print(request.form.get('comentario'))
        
        if request.form.get('estrellas') == None or request.form.get('comentario') == "":
            flash('Debe calificar y agregar un comentario', 'warning')
        else:
            calificacion = request.form["estrellas"]
            comment = request.form["comentario"]
            codproducto= request.form["codprod"]
            username = 'jperez'
            fecha = datetime.today().strftime("%b %d %Y %H:%M:%S")
            sql = "INSERT INTO tblComentarios(nombreUsuario, codigoProducto, calificacion, comentario, fecha) VALUES (?, ?, ?, ?, ?)"
            # Ejecutar la consulta
            res = accion(sql,(username, codproducto, calificacion, comment, fecha))
            if res!=0:
                flash('Registro guardado exitosamente!','success')
            else:
                flash('Error al guardar el registro, revise los datos','error')
        return redirect(url_for('comentar'))   

@app.route('/admin/anadirproductos', methods=['GET', 'POST'])
def anadirproducto():
    if request.method == 'GET':
        return render_template('anadirProducto.html', titulo= 'Añadir Producto | VipShop')
    else:
        pass
        #Registrar nuevo producto en la BD y mostrarlo en la vista productos

@app.route('/admin/deleteproduct', methods=['GET', 'POST'])
def eliminarproducto():
    if request.method == 'GET':
        return render_template('deleteProduct.html', titulo= 'Eliminar Producto | VipShop')
    else:
        pass
        #Eliminar producto en la BD y retornar a pagina de elminación.

@app.route('/wishlist', methods=['GET', 'POST'])
def wishlist():
    if request.method == 'GET':
        return render_template('wishlist.html', titulo= 'Favoritos | VipShop')
    else:
        pass
        #Agregar producto a lista de deseos

if __name__ == '__main__':
    app.run(debug=True)
