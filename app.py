from flask import Flask, render_template, request
from types import SimpleNamespace
import json

import os

FICHERO_USUARIOS = "usuarios.json"

def cargar_usuarios_desde_json():
    if not os.path.exists(FICHERO_USUARIOS):
        return []

    with open(FICHERO_USUARIOS, "r", encoding="utf-8") as f:
        contenido = f.read().strip()
        if not contenido:
            return []

        # JSON -> lista de objetos (SimpleNamespace)
        return json.loads(contenido, object_hook=lambda d: SimpleNamespace(**d))


def guardar_usuarios_a_json(usuarios):
    usuarios_dict = [u.__dict__ for u in usuarios]
    with open(FICHERO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(usuarios_dict, f, indent=4, ensure_ascii=False)

app = Flask(__name__)

# Lista en memoria (por ahora)
usuarios = cargar_usuarios_desde_json()


@app.route("/", methods=["GET", "POST"])
def crear_usuario():

    if request.method == "POST":
        usuario = SimpleNamespace(
            email=request.form["email"],
            nombre=request.form["nombre"],
            apellidos=request.form["apellidos"],
            password=request.form["password"],
            telefono=request.form["telefono"],
            edad=request.form["edad"]
        )

        usuarios.append(usuario)
        guardar_usuarios_a_json(usuarios)


        return f"""
        <h2>Usuario guardado en JSON</h2>
        <p>Total usuarios en memoria: {len(usuarios)}</p>
        <a href="/">Volver</a>
        """

    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
