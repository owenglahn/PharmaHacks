from flask import Flask, redirect, render_template, request, url_for

@app.route('/', methods = ["GET"])
def index():
    return 