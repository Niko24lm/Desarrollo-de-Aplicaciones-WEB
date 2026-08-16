const formulario = document.getElementById("formRegistro");
const lista = document.getElementById("lista");
const mensaje = document.getElementById("mensaje");
const total = document.getElementById("total");

const servicios = [];

let contador = 0;

function validarNombre(){

    const nombre = document.getElementById("nombre");

    const error = document.getElementById("errorNombre");

    if(nombre.value.trim().length < 3){

        nombre.classList.add("is-invalid");

        nombre.classList.remove("is-valid");

        error.textContent = "Debe tener al menos 3 caracteres.";

        return false;

    }

    nombre.classList.remove("is-invalid");

    nombre.classList.add("is-valid");

    error.textContent="";

    return true;

}

function validarDescripcion(){

    const descripcion = document.getElementById("descripcion");

    const error = document.getElementById("errorDescripcion");

    if(descripcion.value.trim().length < 10){

        descripcion.classList.add("is-invalid");

        descripcion.classList.remove("is-valid");

        error.textContent="La descripción debe tener al menos 10 caracteres.";

        return false;

    }

    descripcion.classList.remove("is-invalid");

    descripcion.classList.add("is-valid");

    error.textContent="";

    return true;

}

function validarCategoria(){

    const categoria=document.getElementById("categoria");

    const error=document.getElementById("errorCategoria");

    if(categoria.value===""){

        categoria.classList.add("is-invalid");

        categoria.classList.remove("is-valid");

        error.textContent="Seleccione una categoría.";

        return false;

    }

    categoria.classList.remove("is-invalid");

    categoria.classList.add("is-valid");

    error.textContent="";

    return true;

}
function mostrarServicios() {

    lista.innerHTML = "";

    if (servicios.length === 0) {

        lista.innerHTML = `
            <div class="alert alert-warning">
                No existen registros.
            </div>
        `;

        total.textContent = 0;

        return;
    }

    servicios.forEach(function(servicio, index) {

        const card = document.createElement("div");

        card.className = "card p-3 my-3 shadow";

        card.innerHTML = `
            <h5>${servicio.nombre}</h5>
            <p>${servicio.descripcion}</p>
            <span class="badge bg-primary">${servicio.categoria}</span>

            <br><br>

            <button class="btn btn-danger eliminar">
                Eliminar
            </button>
        `;

        card.querySelector(".eliminar").addEventListener("click", function() {

            servicios.splice(index, 1);

            mostrarServicios();

        });

        lista.appendChild(card);

    });

    total.textContent = servicios.length;

}
formulario.addEventListener("submit", function(e) {

    e.preventDefault();

    if(
    !validarNombre() ||
    !validarDescripcion() ||
    !validarCategoria()
){
    return;
}

    const nombre = document.getElementById("nombre").value;
    const descripcion = document.getElementById("descripcion").value;
    const categoria = document.getElementById("categoria").value;

    if (nombre === "" || descripcion === "" || categoria === "") {

        mensaje.innerHTML =
        "<div class='alert alert-danger'>Todos los campos son obligatorios.</div>";

        return;
    }

    mensaje.innerHTML =
    "<div class='alert alert-success'>Registro agregado correctamente.</div>";

   servicios.push({
    nombre: nombre,
    descripcion: descripcion,
    categoria: categoria
});

mostrarServicios();

formulario.reset();

 document.getElementById("nombre").addEventListener("input", validarNombre);

document.getElementById("descripcion").addEventListener("input", validarDescripcion);

document.getElementById("categoria").addEventListener("change", validarCategoria);

});
mostrarServicios();