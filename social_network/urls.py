from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


# Главная страница
def home_view(request):
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Social Network API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f0f2f5;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 2px 15px rgba(0,0,0,0.1);
                text-align: center;
            }
            h1 {
                color: #1877f2;
                font-size: 2.5em;
                margin-bottom: 20px;
            }
            .status {
                background: #42b72a;
                color: white;
                padding: 12px 24px;
                border-radius: 8px;
                display: inline-block;
                font-size: 1.2em;
                margin: 20px 0;
            }
            .links {
                margin: 30px 0;
            }
            .links a {
                display: inline-block;
                background: #1877f2;
                color: white;
                padding: 12px 24px;
                margin: 10px;
                text-decoration: none;
                border-radius: 6px;
                font-size: 1.1em;
                transition: background 0.3s;
            }
            .links a:hover {
                background: #165eab;
            }
            .api-list {
                text-align: left;
                background: #f8f9fa;
                padding: 20px;
                border-radius: 8px;
                margin: 30px 0;
            }
            .api-list h3 {
                color: #333;
                margin-top: 0;
            }
            .endpoint {
                margin: 10px 0;
                padding: 10px;
                background: white;
                border-left: 4px solid #1877f2;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>📱 Social Network API</h1>
            <p>Бэкенд для социальной сети обмена фотографиями</p>

            <div class="status">✅ Сервер успешно запущен!</div>

            <div class="links">
                <a href="/admin/">Админ-панель</a>
                <a href="/api/posts/">API Постов</a>
                <a href="/api-auth/login/">Войти в API</a>
            </div>

            <div class="api-list">
                <h3>📋 Доступные эндпоинты:</h3>
                <div class="endpoint"><strong>GET /api/posts/</strong> - Получить все посты</div>
                <div class="endpoint"><strong>POST /api/posts/</strong> - Создать пост</div>
                <div class="endpoint"><strong>GET /api/posts/{id}/</strong> - Получить пост по ID</div>
                <div class="endpoint"><strong>POST /api/posts/{id}/like/</strong> - Поставить лайк</div>
                <div class="endpoint"><strong>POST /api/posts/{id}/unlike/</strong> - Убрать лайк</div>
                <div class="endpoint"><strong>GET /api/comments/</strong> - Все комментарии</div>
                <div class="endpoint"><strong>POST /api/comments/</strong> - Создать комментарий</div>
            </div>

            <p style="color: #666; margin-top: 30px;">
                Дипломный проект • Django REST Framework
            </p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)


urlpatterns = [
    path('', home_view, name='home'),  # Главная страница
    path('admin/', admin.site.urls),
    # Пока что закомментируем эти строки - добавим позже
    # path('api/', include('posts.urls')),
    # path('api-auth/', include('rest_framework.urls')),
]

# Для обслуживания медиафайлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)