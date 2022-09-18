#!/usr/bin/python3
#
# The Website of wrap4u@wallisch-it.net implemented in Python hosted by Flask.
#
from flask import Flask, send_from_directory
from flask import request
from flask import render_template
import json

webapp = Flask(__name__, template_folder="app_python")

SPEISEN = [
    {"id":101,  "name":"Wrap-Teigfladen",   "preis":1.00,   "aktiv":True },
    {"id":102,  "name":"Tortilla-Chips",    "preis":1.00,   "aktiv":True },
    {"id":103,  "name":"Burger_Bun",        "preis":1.50,   "aktiv":False }    
]

SAUCEN = [
    {"id":201,  "name":"Burger-Sauce",          "preis":0.50,   "aktiv":True },
    {"id":202,  "name":"Curry-Mango-Sauce",     "preis":0.50,   "aktiv":True },
    {"id":203,  "name":"Schnittlauchrahm",      "preis":0.50,   "aktiv":True },
    {"id":204,  "name":"Tabasco",               "preis":0.50,   "aktiv":True }
]

BEILAGEN = [
    {"id":301,  "name":"Haferflockenbällchen",  "preis":0.50,   "aktiv":True },
    {"id":302,  "name":"Tofu",                  "preis":0.50,   "aktiv":True },
    {"id":303,  "name":"Champions-gebraten",    "preis":0.50,   "aktiv":True },
    {"id":304,  "name":"Zuchini-gebraten",      "preis":0.50,   "aktiv":True },
]

GEMUESE = [
    {"id":401,  "name":"Avocado",               "preis":0.50,   "aktiv":True },
    {"id":402,  "name":"Bohnen",                "preis":0.50,   "aktiv":True },
    {"id":403,  "name":"Gurke",                 "preis":0.50,   "aktiv":True },
    {"id":404,  "name":"Mais",                  "preis":0.50,   "aktiv":True },

    {"id":405,  "name":"Paprika",               "preis":0.50,   "aktiv":True },
    {"id":406,  "name":"Tomate",                "preis":0.50,   "aktiv":True },
    {"id":407,  "name":"Eisbergsalat",          "preis":0.50,   "aktiv":True },
    {"id":408,  "name":"Vogerlsalat",           "preis":0.50,   "aktiv":True },

    {"id":409,  "name":"karamelisierter-Zwiebel",   "preis":0.50,   "aktiv":True },
]


BESTELLUNGEN = []

# Templates
@webapp.route("/index.html")
def send_index():
    return render_template("index.html")

@webapp.route("/neu.html")
def send_neu():
    return render_template("neu.html", speisen=SPEISEN, saucen=SAUCEN, beilagen=BEILAGEN, gemuesen=GEMUESE)

# Deliver static content
@webapp.route("/<path:path>")
def send_static(path):
    return send_from_directory('static', path)

# The main-page
@webapp.route("/")
def main():
    return render_template("index.html")

if __name__ == "__main__":
    webapp.run(host="0.0.0.0", port=8080)
