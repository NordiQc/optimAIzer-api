from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    cpu = data.get("cpu", "")
    gpu = data.get("gpu", "")
    ram = data.get("ram", "")
    storage = data.get("storage", "")
    os_version = data.get("os", "")
    use_case = data.get("use_case", "")

    critique = []
    important = []
    optionnel = []

    if "hdd" in storage.lower():
        important.append("T’as un foutu HDD... change-moi ça pour un SSD, pis ça va rouler pas mal plus smooth.")

    try:
        ram_value = int(ram.replace("Go", "").replace("GB", "").strip())
        if ram_value < 16:
            important.append("8 Go de RAM c’est ben juste – 16 Go, minimum, surtout pour gamer.")
    except:
        optionnel.append("Impossible de lire la RAM — écris ça plus clairement mon chum.")

    if "i3" in cpu.lower() or "ryzen 3" in cpu.lower():
        critique.append("Ton CPU est aussi rapide qu’un escargot dans le sable – upgrade ça là, tabarouette!")

    optionnel.append("Désactive donc les effets visuels dans Windows, c’est cute mais ça sert à rien.")
    optionnel.append("Y’a sûrement des gugusses qui partent au démarrage. Nettoie ça avec Ccleaner.")

    return jsonify({
        "critique": critique,
        "important": important,
        "optionnel": optionnel
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
