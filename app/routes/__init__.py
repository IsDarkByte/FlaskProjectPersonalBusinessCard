from flask import Flask

def create_app():
    """
    Фабрика создания Flask-приложения.
    Используется для организации кода и масштабирования.
    """
    app = Flask(__name__)

    # Импорт и регистрация блупринтов (модулей с маршрутами)
    from .routes.main import main_bp
    from .routes.projects import projects_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(projects_bp)

    return app
