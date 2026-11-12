import os
import random
import logging
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

EXCUSES = [
    "My WiFi died mid-lecture and took my motivation with it.",
    "My cat deleted my assignment.",
    "I was stuck in a traffic jam of my own thoughts.",
    "My alarm rang. I negotiated with it. I lost.",
    "I studied all night, but only in my dreams.",
    "My laptop updated for 4 hours and I couldn't stop it.",
    "I was busy saving the world. Boring details, sorry.",
    "The bus left early, or I woke up late. Hard to say.",
    "I wrote the whole thing, then my pen ran out of ink.",
    "I thought today was Sunday. Everything felt too peaceful.",
]

visits = 0
APP_ENV = os.environ.get("APP_ENV", "local")


@app.route("/")
def home():
    global visits
    visits += 1
    log.info("Home page visit #%d", visits)
    return render_template("index.html", visits=visits, env=APP_ENV)


@app.route("/api/excuse")
def excuse():
    name = request.args.get("name", "").strip()[:30] or "Student"
    pick = random.choice(EXCUSES)
    log.info("Excuse generated for %s: %s", name, pick)
    return jsonify(name=name, excuse=pick)


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    app.run(debug=True)