from flask import Blueprint, render_template
from app.cache import cache
import requests
import os


projects_bp = Blueprint('projects', __name__)

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "IsDarkByte")

@projects_bp.route("/projects")
@cache.cached(timeout=300)  # кеш на 5 минут
def projects():
    """
    Загружаем проекты с GitHub и кешируем результат на 5 минут.
    """
    url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        repos = response.json()
    else:
        repos = []
    return render_template("projects.html", repos=repos)
