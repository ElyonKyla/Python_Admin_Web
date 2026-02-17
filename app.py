from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def crear_usuario():

    if request.method == "POST":
        email = request.form["email"]
        nombre = request.form["nombre"]
        apellidos = request.form["apellidos"]
        password = request.form["password"]
        telefono = request.form["telefono"]
        edad = request.form["edad"]

        return f"""
        <h2>Usuario recibido</h2>
        <p>Email: {email}</p>
        <p>Nombre: {nombre}</p>
        <p>Apellidos: {apellidos}</p>
        <p>Teléfono: {telefono}</p>
        <p>Edad: {edad}</p>
        <a href="/">Volver</a>
        """

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
