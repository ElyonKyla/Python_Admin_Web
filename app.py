from flask import Flask, render_template, request
from types import SimpleNamespace

app = Flask(__name__)

# Lista en memoria (por ahora)
usuarios = []

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

        return f"""
        <h2>Usuario guardado en memoria</h2>
        <p>Total usuarios en memoria: {len(usuarios)}</p>
        <a href="/">Volver</a>
        """

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
