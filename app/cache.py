from flask_caching import Cache

# Конфигурация кеша: тип Simple (в памяти)
cache = Cache(config={
    "CACHE_TYPE": "SimpleCache",  # Можно заменить на Redis, если будет нужно
    "CACHE_DEFAULT_TIMEOUT": 300  # Время жизни кеша: 300 сек (5 мин)
})
