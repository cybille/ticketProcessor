from parseResp import parse
from prompt import processUserQuery
from flask import Flask, redirect, render_template, request, url_for

app= Flask(__name__)
app.config.from_object('config.config')


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/ticketForm",  methods=("GET", "POST"))
def ticketform():
    return processUserQuery("IT professions")

@app.route("/ticketResponse",  methods=("GET", "POST"))
def ticketResponse():
    return parse(processUserQuery("IT professions"))


