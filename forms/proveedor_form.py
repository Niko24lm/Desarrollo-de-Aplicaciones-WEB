from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class ProveedorForm(FlaskForm):

    nombre = StringField(
        "Nombre del proveedor",
        validators=[
            DataRequired(message="El nombre es obligatorio"),
            Length(min=3, max=100, message="Debe tener entre 3 y 100 caracteres")
        ]
    )

    correo = EmailField(
        "Correo electrónico",
        validators=[
            DataRequired(message="El correo es obligatorio"),
            Email(message="Ingrese un correo válido")
        ]
    )

    telefono = StringField(
        "Teléfono",
        validators=[
            DataRequired(message="El teléfono es obligatorio"),
            Length(min=7, max=20, message="Ingrese un teléfono válido")
        ]
    )

    submit = SubmitField("Guardar proveedor")