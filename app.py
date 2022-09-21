#coding: utf-8
from flask import Flask
app = Flask("PROJETO")
@app.route(";")
def ola_mundo():
    return "Olá Mundo! Esse é o primeiro projetinho Flask, 200"
app.run()