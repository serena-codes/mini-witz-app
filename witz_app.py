import tkinter as tk
import pyjokes
import random
import requests

# Lokale Witz-Funktion (Pyjokes)
def zeige_witze():
    farben = ["#FFFAE3", "#E0FFFF", "#FFF0F5", "#F0FFF0"]
    emojis = ["😄", "😎", "🙃", "😊"]
    farbe = random.choice(farben)
    emoji = random.choice(emojis)

    jokes = pyjokes.get_jokes(language='de', category='neutral')
    zufallswitze = random.sample(jokes, min(3, len(jokes)))

    textfeld.config(
        text=f"{emoji}\n" + "\n\n".join(zufallswitze),
        bg=farbe,
        font=("Segoe UI Emoji", 12)
    )

# Online-Witz-Funktion (WitzAPI.de)
def zeige_witzapi():
    farben = ["#FFFAE3", "#E0FFFF", "#FFF0F5", "#F0FFF0"]
    farbe = random.choice(farben)

    try:
        url = "https://witzapi.de/api/joke/?limit=1"
        response = requests.get(url, timeout=5)
        daten = response.json()
        if daten and "text" in daten[0]:
            witz = daten[0]["text"]
            textfeld.config(
                text=f"{witz}\n\n🌐 WitzAPI.de",
                bg=farbe,
                font=("Arial", 12)
            )
        else:
            raise ValueError("Keine Witze erhalten")
    except:
        fallback = "API nicht erreichbar – vielleicht ein Witz aus der Steckdose?"
        textfeld.config(text=f"{fallback}\n\n⚠️ Quelle: Offline", bg=farbe)

# Fenster erstellen
fenster = tk.Tk()
fenster.title("Lach mal wieder! 😄")
fenster.geometry("520x420")

# Überschrift
titel = tk.Label(fenster, text="Witz-Generator", font=("Comic Sans MS", 20, "bold"), fg="#FF5733")
titel.pack(pady=3)

# Textfeld für Witze
textfeld = tk.Label(fenster, text="Drück den Knopf für Witze!", wraplength=480, justify="left", font=("Arial", 12))
textfeld.pack(pady=15)

# Button für lokale Witze
knopf_local = tk.Button(fenster, text="Witze anzeigen 😄", command=zeige_witze, bg="#FFD700", fg="black", font=("Arial", 12, "bold"))
knopf_local.pack(pady=5)

# Button für API-Witze
knopf_api = tk.Button(fenster, text="Zugabe? 🌐", command=zeige_witzapi, bg="#ADD8E6", fg="black", font=("Arial", 12, "bold"))
knopf_api.pack(pady=5)

# GUI starten
fenster.mainloop()