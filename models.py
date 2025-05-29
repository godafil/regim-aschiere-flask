MATERIALE = {
    "Oțel moale": {"duritate": 160, "k_c": 1600},
    "Oțel călit": {"duritate": 300, "k_c": 2200},
    "Fontă": {"duritate": 200, "k_c": 1800},
    "Aluminiu": {"duritate": 80, "k_c": 900},
    "Inox": {"duritate": 250, "k_c": 2000}
}

SCULE = {
    "Freză HSS Ø10, 4 dinți": {"diametru": 10, "nr_dinti": 4, "material": "HSS"},
    "Freză carburi Ø12, 3 dinți": {"diametru": 12, "nr_dinti": 3, "material": "carburi"},
    "Burghiu Ø8 HSS, 2 dinți": {"diametru": 8, "nr_dinti": 2, "material": "HSS"},
    "Freză Ø6 carburi, 2 dinți": {"diametru": 6, "nr_dinti": 2, "material": "carburi"},
    "Freză Ø16 HSS, 6 dinți": {"diametru": 16, "nr_dinti": 6, "material": "HSS"}
}

class Material:
    def __init__(self, nume, duritate, k_c):
        self.nume = nume
        self.duritate = duritate
        self.k_c = k_c

class Scula:
    def __init__(self, tip, diametru, nr_dinti, material_scula):
        self.tip = tip
        self.diametru = diametru
        self.nr_dinti = nr_dinti
        self.material = material_scula

class Semifabricat:
    def __init__(self, lungime, latime, inaltime, material):
        self.lungime = lungime
        self.latime = latime
        self.inaltime = inaltime
        self.material = material

class RegimDeAschiere:
    def __init__(self, semifabricat, scula, adancime, avans_dinte):
        self.semifabricat = semifabricat
        self.scula = scula
        self.adancime = adancime
        self.avans_dinte = avans_dinte

    def calculeaza(self):
        Vc = self.semifabricat.material.k_c / 1000
        D = self.scula.diametru
        n = (1000 * Vc) / (3.14 * D) if D > 0 else 0
        f_m = self.avans_dinte * self.scula.nr_dinti * n
        F_c = self.semifabricat.material.k_c * self.adancime * f_m / 1000
        F_f = F_c * 0.25
        F_r = F_c * 0.15
        return Vc, n, f_m, F_c, F_f, F_r