from flask import Flask, render_template, request, flash, redirect
from app import app
from data import db_articles
import shoebox

import os

temp = ["ndb"]
articles = db_articles(temp)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    url = request.form['url']

    if len(url) > 0:
        print(url)
        temp = shoebox.classify_image_url(url)
        print(temp)
    else:
        target = os.path.join(APP_ROOT, 'images/')
        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)

        for file in request.files.getlist("file"):
            print(file)
            filename = file.filename
            print(filename)
            destination = "/".join([target, filename])
            print(destination)
            file.save(destination)
            temp = shoebox.classify_local_image(url)
            print(temp)

        url = destination
        print(url)

    return render_template("result.html", url=url, articles=db_articles(temp))

