from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class FacturacionForm(FlaskForm):

    cliente = StringField(
        "Cliente",
        validators=[
            DataRequired(message="El cliente es obligatorio")
        ]
    )

    producto = StringField(
        "Producto",
        validators=[
            DataRequired(message="El producto es obligatorio")
        ]
    )

    total = FloatField(
        "Total",
        validators=[
            DataRequired(message="El total es obligatorio"),
            NumberRange(min=0, message="El total no puede ser negativo")
        ]
    )

    submit = SubmitField("Guardar factura")