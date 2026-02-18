from flask import Flask, render_template, request, redirect
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


@app.route("/crear", methods=["GET", "POST"])
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

@app.route("/usuarios")
def listar_usuarios():
    usuarios = cargar_usuarios_desde_json()
    return render_template("usuarios.html", usuarios=usuarios)

print("ROUTES:", app.url_map)

@app.route("/")
def menu():
    return render_template("menu.html")

@app.route("/borrar/<email>")
def borrar_usuario(email):
    usuarios = cargar_usuarios_desde_json()
    usuarios = [u for u in usuarios if u.email != email]
    guardar_usuarios_a_json(usuarios)
    return redirect("/usuarios")

@app.route("/editar/<email>")
def editar_usuario(email):
    usuarios = cargar_usuarios_desde_json()
    usuario = next((u for u in usuarios if u.email == email), None)

    if usuario is None:
        return "<h2>Usuario no encontrado</h2><a href='/usuarios'>Volver</a>"

    return render_template("editar.html", usuario=usuario)

@app.route("/editar_guardar/<email>", methods=["POST"])
def editar_guardar(email):
    usuarios = cargar_usuarios_desde_json()

    for u in usuarios:
        if u.email == email:
            u.nombre = request.form["nombre"]
            u.apellidos = request.form["apellidos"]
            u.password = request.form["password"]
            u.telefono = request.form["telefono"]
            u.edad = request.form["edad"]
            break

    guardar_usuarios_a_json(usuarios)
    return redirect("/usuarios")

if __name__ == "__main__":
    app.run(debug=True)
