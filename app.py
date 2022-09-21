#coding: utf-8
from flask import Flask, render_template
app = Flask("PROJETO")
@app.route("/")
def ola_mundo():
    #criar variavel nome
    nome="Vitor Esbrolio Lima"
    return render_template("alo.html", n=nome), 200
app.run()