from flask import Flask, render_template

app = Flask(__name__)

# Datos de ejemplo
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


# Página principal
@app.route("/")
def inicio():

    mensaje = "Bienvenido al Sistema de Gestión Web"

    resumen = {
        "productos": len(productos),
        "clientes": len(clientes),
        "proveedores": len(proveedores),
        "facturas": len(facturas)
    }

    return render_template(
        "index.html",
        mensaje=mensaje,
        resumen=resumen
    )


# Productos
@app.route("/productos")
def pagina_productos():

    return render_template(
        "productos.html",
        productos=productos
    )


# Clientes
@app.route("/clientes")
def pagina_clientes():

    return render_template(
        "clientes.html",
        clientes=clientes
    )


# Proveedores
@app.route("/proveedores")
def pagina_proveedores():

    return render_template(
        "proveedores.html",
        proveedores=proveedores
    )


# Facturación
@app.route("/facturacion")
def pagina_facturacion():

    return render_template(
        "facturacion.html",
        facturas=facturas
    )


if __name__ == "__main__":
    app.run(debug=True)