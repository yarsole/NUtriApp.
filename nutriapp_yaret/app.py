from flask import Flask, render_template, request, redirect

app = Flask(__name__)

usuarios = {}

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/registrar", methods=["GET","POST"])
def registrar():
    if request.method == "POST":
        user = request.form["usuario"]
        pw = request.form["password"]
        usuarios[user] = pw
        return redirect("/entrar")
    return render_template("registrar.html")

@app.route("/entrar", methods=["GET","POST"])
def entrar():
    if request.method == "POST":
        user = request.form["usuario"]
        pw = request.form["password"]

        if user in usuarios and usuarios[user] == pw:
            return redirect("/")
        else:
            return "Usuario o contraseña incorrectos"
    return render_template("entrar.html")

@app.route("/aprende")
def aprende():
    return render_template("aprende.html")

@app.route("/platillos")
def platillos():
    return render_template("platillos.html")

@app.route("/opciones")
def opciones():
    return render_template("opciones.html")

@app.route("/balance", methods=["GET","POST"])
def balance():
    macros = None

    if request.method == "POST":
        peso = float(request.form["peso"])
        altura = float(request.form["altura"])
        edad = float(request.form["edad"])
        sexo = request.form["sexo"]

        if sexo == "hombre":
            tmb = 10*peso + 6.25*altura - 5*edad + 5
        else:
            tmb = 10*peso + 6.25*altura - 5*edad - 161

        calorias = tmb * 1.4

        macros = {
            "proteina": round((calorias * 0.3) / 4),
            "carbos": round((calorias * 0.45) / 4),
            "grasas": round((calorias * 0.25) / 9)
        }

    return render_template("balance.html", macros=macros)

@app.route("/metapeso", methods=["GET","POST"])
def metapeso():
    pesoideal = None

    if request.method == "POST":
        altura = float(request.form["altura"])
        pesoideal = round((altura - 100) * 0.9)

    return render_template("metapeso.html", pesoideal=pesoideal)

if __name__ == "__main__":
    app.run(debug=True)
