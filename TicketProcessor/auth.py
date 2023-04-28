from flask import Flask, redirect, render_template, request, url_for
from flask import Blueprint #for user authenticatiion

auth_bp= Blueprint('auth_bp', __name__)

@auth_bp.route("/signin",  methods=("GET", "POST"))
def signin():
    return "hello"

@auth_bp.route("/signup",  methods=("GET", "POST"))
def signup():
    return "hello"

