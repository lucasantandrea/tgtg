import sys
import os

# Aggiungi il percorso al modulo __main__.py
sys.path.append(os.path.dirname(__file__))

# Importa il modulo __main__
import __main__



------------------

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/run-script', methods=['GET'])
def run_script():
    # Esegui una funzione dal modulo __main__.py
    risultato = __main__.main()
    return jsonify({"message": "Script eseguito con successo!", "result": risultato})

if __name__ == '__main__':
    app.run(debug=True)

