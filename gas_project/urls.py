from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Sabse Zaroori Line: Hum gas_app se views mangwa rahe hain
from gas_app import views 

urlpatterns = [
    # Admin Panel
    path('admin/', admin.site.urls),

    # Website Pages
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard & Booking
    path('dashboard/', views.dashboard, name='dashboard'),
    path('book/', views.book, name='book'),

    # Status Update (Admin ke liye)
    path('update-status/<int:order_id>/', views.update_order_status, name='update_order_status'),
]

# Images (Static Files) ke liye zaroori setting
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)