from flask import Flask, render_template

app = Flask(__name__)

fruits_list = [
    {"name": "Яблуко", "color": "red", "image": "/static/  .jpg"},
    {"name": "Вишня", "color": "red", "image": "/static/cherry.jpg"},
    {"name": "Банан", "color": "yellow", "image": "/static/banana.jpg"},
    {"name": "Апельсин", "color": "orange", "image": "/static/orange.jpg"},
    {"name": "Груша", "color": "green", "image": "/static/pear.jpg"},
    {"name": "Ківі", "color": "green", "image": "/static/kivi.jpg"},
]





@app.route("/")
def all_fruits():
    return render_template("homeworkof8.3.html", fruits=fruits_list)

@app.route("/red")
def red_fruits():
    return render_template("homeworkof8.3.html", fruits=[
        {"name": "Яблуко", "color": "red", "image": "/static/  .jpg"},
        {"name": "Вишня", "color": "red", "image": "/static/cherry.jpg"},
    ])
@app.route("/green")
def green_fruits():
    return render_template("homeworkof8.3.html", fruits=[
        {"name": "Груша", "color": "green", "image": "/static/pear.jpg"},
        {"name": "Ківі", "color": "green", "image": "/static/kivi.jpg"},
    ])
@app.route("/yellowfruitsandorangefruits")
def yellow_and_orange_fruits():
    return render_template("homeworkof8.3.html", fruits=[
        {"name": "Апельсин", "color": "orange", "image": "/static/orange.jpg"},
        {"name": "Банан", "color": "yellow", "image": "/static/banana.jpg"}
    ])

if __name__ == "__main__":
    app.run(debug=True)
