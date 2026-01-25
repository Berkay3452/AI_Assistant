import logging
from flask import Flask, jsonify
from flask_cors import CORS
import threading

# 1. Gereksiz logları kapat (Terminal temiz kalsın)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app = Flask(__name__)
CORS(app) # HTML'in buraya erişmesine izin ver

# 2. Asistanın Durumu (Başlangıçta boşta)
# Durumlar: "idle" (Bekliyor), "speaking" (Konuşuyor), "listening" (Dinliyor)
current_status = "idle"

# 3. HTML Burayı Okur (Saniyede 2 kez)
@app.route('/status', methods=['GET'])
def get_status():
    global current_status
    return jsonify({'status': current_status})

# 4. Main.py Burayı Kullanır (Durumu değiştirmek için)
def set_state(new_state):
    global current_status
    current_status = new_state

# 5. Sunucuyu Başlatma Kodları
def run_server():
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

def start():
    t = threading.Thread(target=run_server)
    t.daemon = True # Ana program kapanınca bu da kapansın
    t.start()
    