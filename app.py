from flask import Flask, render_template, request
from models import Material, Scula, Semifabricat, RegimDeAschiere
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nume_material = request.form["nume_material"]
        duritate = float(request.form["duritate"])
        k_c = float(request.form["k_c"])
        lungime = float(request.form["lungime"])
        latime = float(request.form["latime"])
        inaltime = float(request.form["inaltime"])
        tip_scula = request.form["tip_scula"]
        diametru = float(request.form["diametru"])
        nr_dinti = int(request.form["nr_dinti"])
        mat_scula = request.form["mat_scula"]
        adancime = float(request.form["adancime"])
        avans_dinte = float(request.form["avans_dinte"])

        mat = Material(nume_material, duritate, k_c)
        semi = Semifabricat(lungime, latime, inaltime, mat)
        scula = Scula(tip_scula, diametru, nr_dinti, mat_scula)
        regim = RegimDeAschiere(semi, scula, adancime, avans_dinte)

        Vc, n, f_m, F_c, F_f, F_r = regim.calculeaza()

        fig, ax = plt.subplots()
        ax.add_patch(plt.Rectangle((0, 0), lungime, latime, edgecolor='blue', facecolor='lightblue', label='Semifabricat'))
        ax.add_patch(plt.Rectangle((0, 0), lungime, adancime, edgecolor='red', facecolor='none', linestyle='--', label='Adâncime'))
        ax.set_title("Schiță semifabricat")
        ax.set_xlabel("Lungime [mm]")
        ax.set_ylabel("Lățime [mm]")
        ax.legend()
        ax.axis("equal")
        plt.grid(True)
        plt.savefig("static/schita.png")
        plt.close()

        return render_template("rezultat.html", Vc=Vc, n=n, f_m=f_m, F_c=F_c, F_f=F_f, F_r=F_r)

    return render_template("index.html")