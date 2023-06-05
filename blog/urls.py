from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from blog import views
from portfolio import views as v

app_name = 'blog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.all_blogs,name="all_blog"),
    path('<int:blog_id>/', views.detail,name="detail"),

]
