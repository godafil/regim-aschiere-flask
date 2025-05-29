from flask import Flask, render_template, request
from models import MATERIALE, SCULE, Material, Scula, Semifabricat, RegimDeAschiere
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.offline as pyo

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", materiale=MATERIALE, scule=SCULE)

@app.route("/calculeaza", methods=["POST"])
def calculeaza():
    material_sel = request.form["material"]
    scula_sel = request.form["scula"]
    lungime = float(request.form["lungime"])
    latime = float(request.form["latime"])
    inaltime = float(request.form["inaltime"])
    adancime = float(request.form["adancime"])
    avans_dinte = float(request.form["avans_dinte"])

    mat_data = MATERIALE[material_sel]
    scula_data = SCULE[scula_sel]

    mat = Material(material_sel, mat_data["duritate"], mat_data["k_c"])
    semi = Semifabricat(lungime, latime, inaltime, mat)
    scula = Scula(scula_sel, scula_data["diametru"], scula_data["nr_dinti"], scula_data["material"])
    regim = RegimDeAschiere(semi, scula, adancime, avans_dinte)

    Vc, n, f_m, F_c, F_f, F_r = regim.calculeaza()

    # Desen static
    fig, ax = plt.subplots()
    ax.add_patch(plt.Rectangle((0, 0), lungime, latime, edgecolor='blue', facecolor='lightblue'))
    ax.add_patch(plt.Rectangle((0, 0), lungime, adancime, edgecolor='red', facecolor='none', linestyle='--'))
    ax.set_title("Schiță semifabricat")
    ax.set_xlabel("Lungime [mm]")
    ax.set_ylabel("Lățime [mm]")
    ax.axis("equal")
    plt.grid(True)
    import os
    os.makedirs("static", exist_ok=True)
    plt.savefig("static/schita.png")
    plt.close()

    # Grafic Plotly
    forta_data = go.Bar(x=["F_c", "F_f", "F_r"], y=[F_c, F_f, F_r], marker=dict(color="royalblue"))
    layout = go.Layout(title="Forțe de așchiere [N]")
    plot_div = pyo.plot(go.Figure(data=[forta_data], layout=layout), output_type="div")

    return render_template("rezultat.html",
                           Vc=Vc, n=n, f_m=f_m, F_c=F_c, F_f=F_f, F_r=F_r,
                           schita="static/schita.png",
                           grafic=plot_div)