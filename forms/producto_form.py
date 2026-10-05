from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange


class ProductoForm(FlaskForm):

    nombre = StringField(
        "Nombre del producto",
        validators=[
            DataRequired(message="El nombre es obligatorio"),
            Length(min=3, max=100, message="Debe tener entre 3 y 100 caracteres")
        ]
    )

    precio = FloatField(
        "Precio",
        validators=[
            DataRequired(message="El precio es obligatorio"),
            NumberRange(min=0, message="El precio no puede ser negativo")
        ]
    )

    stock = IntegerField(
        "Stock",
        validators=[
            DataRequired(message="El stock es obligatorio"),
            NumberRange(min=0, message="El stock no puede ser negativo")
        ]
    )

    submit = SubmitField("Guardar producto")