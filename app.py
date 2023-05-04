from flask import *
import requests
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        print(request.form["id"],"\n",request.form["text"])
        id = request.form["id"]
        text = request.form["text"]
        r = requests.post("http://127.0.0.1:5000/api/update/text", json={"text": text, "id": id})
        print(f"status code: {r.status_code}")

    return render_template("home.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)