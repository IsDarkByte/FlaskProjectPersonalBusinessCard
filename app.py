from flask import Flask, render_template
from flask_caching import Cache
import requests

app = Flask(__name__)

app.config['CACHE_TYPE'] = 'SimpleCache'
app.config['CACHE_DEFAULT_TIMEOUT'] = 600  # 10 минут

cache = Cache(app)

GITHUB_USERNAME = "IslamMuha"

@app.route("/")
def home():
    return render_template("index.html")

@cache.cached(timeout=600)
@app.route("/projects")
def projects():
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    headers = {"User-Agent": "FlaskApp-IslamMuha"}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return render_template("projects.html", repos=response.json())
        else:
            print(f"[❗] Ошибка GitHub API: статус {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[⚠️] Ошибка запроса к GitHub: {e}")
    
    return render_template("projects.html", repos=[])

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run(debug=True)
