from app import create_app
import os

# Создаём экземпляр приложения через фабрику
app = create_app()

# Запускаем сервер в режиме отладки
if __name__ == "__main__":
    app.run( 
        host=os.getenv("FLASK_RUN_HOST", "127.0.0.1"),
        debug=os.getenv("FLASK_ENV") == "development"
        )
