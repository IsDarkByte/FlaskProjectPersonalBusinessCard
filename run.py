from app import create_app

# Создаём экземпляр приложения через фабрику
app = create_app()

# Запускаем сервер в режиме отладки
if __name__ == "__main__":
    app.run(debug=True)
