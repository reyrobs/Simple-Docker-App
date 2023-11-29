from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images

images = ["https://images.pexels.com/photos/1661179/pexels-photo-1661179.jpeg",
          "https://images.pexels.com/photos/17811/pexels-photo.jpg",
          "https://images.pexels.com/photos/2295744/pexels-photo-2295744.jpeg",
          "https://images.pexels.com/photos/3608263/pexels-photo-3608263.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
          "https://images.pexels.com/photos/106686/pexels-photo-106686.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
          "https://images.pexels.com/photos/674318/pexels-photo-674318.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2"]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
