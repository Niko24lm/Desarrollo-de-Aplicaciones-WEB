const formulario = document.getElementById("formRegistro");
const lista = document.getElementById("lista");
const mensaje = document.getElementById("mensaje");
const total = document.getElementById("total");

let contador = 0;

formulario.addEventListener("submit", function(e) {

    e.preventDefault();

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

    const card = document.createElement("div");

    card.className = "card p-3 my-3 shadow";

    card.innerHTML = `
        <h5>${nombre}</h5>
        <p>${descripcion}</p>
        <span class="badge bg-primary">${categoria}</span>

        <br><br>

        <button class="btn btn-danger eliminar">
            Eliminar
        </button>
    `;

    lista.appendChild(card);

    contador++;

    total.textContent = contador;

    card.querySelector(".eliminar").addEventListener("click", function() {

        card.remove();

        contador--;

        total.textContent = contador;

    });

    formulario.reset();

});