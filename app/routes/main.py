from flask import Blueprint, render_template


# Создаём блупринт (модуль маршрутов)
main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    """Главная страница сайта"""
    return render_template("index.html")

@main_bp.route("/about")
def about():
    """Страница 'Обо мне'"""
    return render_template("about.html")

@main_bp.route("/contacts")
def contacts():
    """Страница 'Контакты'"""
    return render_template("contacts.html")
