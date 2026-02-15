from flask import Flask
import qrcode
import os

app = Flask(__name__)

# URL local
url = "http://127.0.0.1:5000/"

# Crear QR
if not os.path.exists("static"):
    os.makedirs("static")

qr = qrcode.make(url)
qr.save("static/qr_yafrank.png")

@app.route("/")
def menu():
    return """
    <html>
    <head>
        <title>YAFRANK - Cevichería</title>
    </head>
    <body style="font-family: Arial; text-align: center; background-color:#f5f5f5;">

        <h1>YAFRANK</h1>
        <h3>Frescura marina todos los días 🐟</h3>

        <hr>

        <h2>Nuestro Menú</h2>

        <img src="/static/menu.jpg" width="80%">

        <br><br>

        <a href="https://wa.me/51940310547?text=Hola%20quiero%20hacer%20un%20pedido%20en%20YAFRANK" target="_blank">
            <button style="padding:15px; background-color:green; color:white; font-size:18px; border:none; border-radius:8px;">
                Pedir por WhatsApp
            </button>
        </a>

        <hr>

        <h3>Escanea para ver el menú</h3>
        <img src="/static/qr_yafrank.png" width="200">

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
