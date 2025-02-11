from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
# Home page
path('', views.home, name='home'),

# Company URLs
path('companies/', views.company_list, name='company_list'),
path('companies/create/', views.company_create, name='company_create'),
path('companies/update/<int:pk>/', views.company_update, name='company_update'),
path('companies/delete/<int:pk>/', views.company_delete, name='company_delete'),
# Product URLs
path('products/', views.product_list, name='product_list'),
path('products/create/', views.product_create, name='product_create'),
path('products/update/<int:pk>/', views.product_update, name='product_update'),
path('products/delete/<int:pk>/', views.product_delete, name='product_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)