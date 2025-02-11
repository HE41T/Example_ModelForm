from django.urls import path
from .views import (
  HomeView,
  CompanyListView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView,
  ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView
)

urlpatterns = [
  path('', HomeView.as_view(), name='home'),

  # Company URLs
  path('companies/', CompanyListView.as_view(), name='company_list'),
  path('companies/create/', CompanyCreateView.as_view(), name='company_create'),
  path('companies/update/<int:pk>/', CompanyUpdateView.as_view(), name='company_update'),
  path('companies/delete/<int:pk>/', CompanyDeleteView.as_view(), name='company_delete'),
  # Product URLs
  path('products/', ProductListView.as_view(), name='product_list'),
  path('products/create/', ProductCreateView.as_view(), name='product_create'),
  path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
  path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]