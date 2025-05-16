from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculeaza', methods=['POST'])
def calculeaza():
    try:
        data = request.get_json()
        duritate = int(data['duritate'])
        diametru = float(data['diametru'])

        viteza = 180 if duritate < 30 else 120 if duritate < 50 else 80
        avans = 0.1 if diametru < 20 else 0.3 if diametru < 50 else 0.5
        adancime = min(2, diametru * 0.05)

        return jsonify({
            'viteza': viteza,
            'avans': avans,
            'adancime': round(adancime, 2)
        })
    except:
        return jsonify({'eroare': 'Date invalide'}), 400