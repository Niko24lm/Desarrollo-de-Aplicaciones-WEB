from flask import Flask, render_template
import sqlite3
import os

from forms.producto_form import ProductoForm
from forms.cliente_form import ClienteForm
from forms.proveedor_form import ProveedorForm
from forms.facturacion_form import FacturacionForm

from flask import Flask, render_template, request, redirect, url_for
from conexion.conexion import obtener_conexion


app = Flask(__name__)

app.config["SECRET_KEY"] = "clave-secreta-proyecto"


# =========================
# BASE DE DATOS
# =========================

def conectar_db():
    ruta_db = os.path.abspath("data/ferreteria.db")
    print("BASE DE DATOS:", ruta_db)

    conn = sqlite3.connect(ruta_db)
    conn.row_factory = sqlite3.Row

    return conn


def inicializar_db():
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect("data/ferreteria.db")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Crear la base de datos y la tabla si no existen
inicializar_db()


# =========================
# DATOS DE EJEMPLO
# =========================

productos = [
    {
        "nombre": "Laptop HP",
        "categoria": "Computación",
        "precio": 850.00,
        "stock": 8
    },
    {
        "nombre": "Mouse inalámbrico",
        "categoria": "Accesorios",
        "precio": 25.50,
        "stock": 15
    },
    {
        "nombre": "Teclado mecánico",
        "categoria": "Accesorios",
        "precio": 48.90,
        "stock": 0
    },
    {
        "nombre": "Monitor 24 pulgadas",
        "categoria": "Monitores",
        "precio": 190.00,
        "stock": 4
    }
]


clientes = [
    {
        "nombre": "Ana Torres",
        "correo": "ana@gmail.com",
        "estado": "Activo"
    },
    {
        "nombre": "Carlos Pérez",
        "correo": "carlos@gmail.com",
        "estado": "Activo"
    },
    {
        "nombre": "María López",
        "correo": "maria@gmail.com",
        "estado": "Inactivo"
    }
]


proveedores = [
    {
        "empresa": "TecnoImport",
        "contacto": "Luis Gómez",
        "telefono": "099111222"
    },
    {
        "empresa": "Digital Supply",
        "contacto": "Sofía Ruiz",
        "telefono": "099333444"
    }
]


facturas = [
    {
        "numero": "F001-001",
        "cliente": "Ana Torres",
        "total": 875.50,
        "estado": "Pagada"
    },
    {
        "numero": "F001-002",
        "cliente": "Carlos Pérez",
        "total": 190.00,
        "estado": "Pendiente"
    },
    {
        "numero": "F001-003",
        "cliente": "María López",
        "total": 48.90,
        "estado": "Anulada"
    }
]


# =========================
# PÁGINA PRINCIPAL
# =========================

@app.route("/")
def inicio():

    mensaje = "Bienvenido al Sistema de Gestión Web"

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) AS total FROM productos")
    total_productos = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM clientes")
    total_clientes = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM proveedores")
    total_proveedores = cursor.fetchone()["total"]

    cursor.execute("SELECT COUNT(*) AS total FROM facturas")
    total_facturas = cursor.fetchone()["total"]

    cursor.close()
    conexion.close()

    resumen = {
        "productos": total_productos,
        "clientes": total_clientes,
        "proveedores": total_proveedores,
        "facturas": total_facturas
    }

    return render_template(
        "index.html",
        mensaje=mensaje,
        resumen=resumen
    )
# =========================
# PRODUCTOS
# =========================

@app.route("/productos")
def pagina_productos():
    print("========== ESTOY USANDO MYSQL ==========")

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_producto,
            nombre,
            precio,
            stock
        FROM productos
    """)

    productos = cursor.fetchall()

    print("PRODUCTOS EN MYSQL:", productos)

    cursor.close()
    conexion.close()

    return render_template(
        "productos.html",
        productos=productos
    )
@app.route("/editar_producto/<int:id_producto>", methods=["GET", "POST"])
def editar_producto(id_producto):

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    if request.method == "POST":

        nombre = request.form["nombre"]
        precio = request.form["precio"]
        stock = request.form["stock"]

        cursor.execute("""
            UPDATE productos
            SET nombre = %s,
                precio = %s,
                stock = %s
            WHERE id_producto = %s
        """, (nombre, precio, stock, id_producto))

        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for("pagina_productos"))

    cursor.execute("""
        SELECT id_producto, nombre, precio, stock
        FROM productos
        WHERE id_producto = %s
    """, (id_producto,))

    producto = cursor.fetchone()

    cursor.close()
    conexion.close()

    return render_template(
        "editar_producto.html",
        producto=producto
    )
@app.route("/eliminar_producto/<int:id_producto>", methods=["POST"])
def eliminar_producto(id_producto):

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        "DELETE FROM productos WHERE id_producto = %s",
        (id_producto,)
    )

    conexion.commit()

    cursor.close()
    conexion.close()

    return redirect(url_for("pagina_productos"))

@app.route("/formulario_producto", methods=["GET", "POST"])
def formulario_producto():

    form = ProductoForm()

    if form.validate_on_submit():

        nombre = form.nombre.data
        precio = form.precio.data
        stock = form.stock.data

        conexion = obtener_conexion()
        cursor = conexion.cursor()

        cursor.execute("""
            INSERT INTO productos (nombre, precio, stock)
            VALUES (%s, %s, %s)
        """, (nombre, precio, stock))

        conexion.commit()

        cursor.close()
        conexion.close()

        return redirect(url_for("pagina_productos"))

    return render_template(
        "formulario_producto.html",
        form=form
    )

# =========================
# CLIENTES
# =========================

@app.route("/clientes")
def pagina_clientes():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_cliente,
            nombre,
            cedula,
            telefono,
            correo
        FROM clientes
        ORDER BY id_cliente
    """)

    clientes_mysql = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template(
        "clientes.html",
        clientes=clientes_mysql
    )

@app.route("/formulario_cliente", methods=["GET", "POST"])
def formulario_cliente():

    form = ClienteForm()

    if form.validate_on_submit():

        nombre = form.nombre.data
        correo = form.correo.data
        telefono = form.telefono.data

        return f"Cliente registrado: {nombre}, Correo: {correo}, Teléfono: {telefono}"

    return render_template(
        "formulario_cliente.html",
        form=form
    )


# =========================
# PROVEEDORES
# =========================

@app.route("/proveedores")
def pagina_proveedores():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            id_proveedor,
            nombre,
            telefono,
            correo
        FROM proveedores
        ORDER BY id_proveedor
    """)

    proveedores_mysql = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template(
        "proveedores.html",
        proveedores=proveedores_mysql
    )


@app.route("/formulario_proveedor", methods=["GET", "POST"])
def formulario_proveedor():

    form = ProveedorForm()

    if form.validate_on_submit():

        nombre = form.nombre.data
        correo = form.correo.data
        telefono = form.telefono.data

        return f"Proveedor registrado: {nombre}, Correo: {correo}, Teléfono: {telefono}"

    return render_template(
        "formulario_proveedor.html",
        form=form
    )


# =========================
# FACTURACIÓN
# =========================

@app.route("/facturacion")
def pagina_facturacion():

    conexion = obtener_conexion()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT
            f.id_factura,
            f.fecha,
            f.total,
            c.nombre AS cliente
        FROM facturas f
        INNER JOIN clientes c
            ON f.id_cliente = c.id_cliente
        ORDER BY f.id_factura
    """)

    facturas_mysql = cursor.fetchall()

    cursor.close()
    conexion.close()

    return render_template(
        "facturacion.html",
        facturas=facturas_mysql
    )
# =========================
# EJECUTAR APLICACIÓN
# =========================

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
   
