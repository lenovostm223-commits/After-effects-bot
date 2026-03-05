from flask import Flask
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return "AMV Bot is running!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

# In main.py: threading.Thread(target=run_flask, daemon=True).start()
