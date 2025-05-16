
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculeaza', methods=['POST'])
def calculeaza():
    try:
        data = request.get_json()
        duritate = int(data['duritate'])
        diametru = float(data['diametru'])
        operatie = data['operatie'].lower()

        # Formule de bază per operație
        if operatie == 'strunjire':
            viteza = 180 if duritate < 30 else 120 if duritate < 50 else 80
            avans = 0.1 if diametru < 20 else 0.3 if diametru < 50 else 0.5
            adancime = min(2, diametru * 0.05)

        elif operatie == 'frezare':
            viteza = 150 if duritate < 30 else 100 if duritate < 50 else 70
            avans = 0.05 if diametru < 20 else 0.2 if diametru < 50 else 0.4
            adancime = min(1.5, diametru * 0.04)

        elif operatie == 'gaurire':
            viteza = 100 if duritate < 30 else 80 if duritate < 50 else 60
            avans = 0.08 if diametru < 20 else 0.25 if diametru < 50 else 0.35
            adancime = min(3, diametru * 0.06)

        else:
            return jsonify({'eroare': 'Operație necunoscută'}), 400

        return jsonify({
            'viteza': viteza,
            'avans': avans,
            'adancime': round(adancime, 2),
            'operatie': operatie
        })
    except:
        return jsonify({'eroare': 'Date invalide'}), 400
