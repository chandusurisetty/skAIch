
from flask import Flask, render_template, request, redirect, url_for
from aiImg import AIImg

import time
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

ai = AIImg()
isImg = False

try:
    os.remove("static/img/aiImg.jpg")
except:
    print("no file")


@app.route("/")
def home():
    return render_template("index.html", isImg=isImg)


@app.route("/generate", methods=["post", "get"])  # type: ignore
def generate():
    if request.method == "POST":
        text = request.form["text"]
        generatedImg = ai.genrateImg(text)

        time.sleep(2)
        if generatedImg:
            global isImg
            isImg = True

            return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
