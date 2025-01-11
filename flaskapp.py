import sys
import os


from flask import Flask, jsonify
import tgtg_scanner.__main__

app = Flask(__name__)

@app.route('/run-script', methods=['GET'])
def run_script():
    # Esegui una funzione dal modulo __main__.py
    risultato = __main__.main()
    return jsonify({"message": "Script eseguito con successo!", "result": risultato})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
