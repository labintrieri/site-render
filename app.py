import os
import requests
from flask import Flask, request

app = Flask (__name__)
BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

@app.route("/")
def index():
  return "Olá, <b> tudo bem </b>?"

@app.route("/teste")
def teste():
  return "Esta página é um <b> teste <b/>!"

@app.route("/telegram", methods = ['POST'])
def telegram_update():
  update= request.json
  url_envio_mensagem = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage" #adicionar em Enviroment
  chat_id = update["message"]["id"]
  mensagem = {"chat_od": chat_id, "text":"mensagem <b>recebida</b>", "parse_mode":"HTML"}
  requests.post(url_envio_mensagem, data = mensagem)
  return "ok"

