from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Company, Product
from .forms import CompanyForm, ProductForm
# หน้าแรก
class HomeView(TemplateView):
  template_name = 'crud_app/home.html'

# Company Views
class CompanyListView(ListView):
  model = Company
  template_name = 'crud_app/company_list.html'
  context_object_name = 'companies'

class CompanyCreateView(CreateView):
  model = Company
  form_class = CompanyForm
  template_name = 'crud_app/company_form.html'
  success_url = reverse_lazy('company_list')

class CompanyUpdateView(UpdateView):
  model = Company
  form_class = CompanyForm
  template_name = 'crud_app/company_form.html'
  success_url = reverse_lazy('company_list')

class CompanyDeleteView(DeleteView):
  model = Company
  template_name = 'crud_app/company_confirm_delete.html'
  success_url = reverse_lazy('company_list')

# Product Views
class ProductListView(ListView):
  model = Product
  template_name = 'crud_app/product_list.html'
  context_object_name = 'products'
  def get_queryset(self):
    # Use `select_related` for better performance
    return Product.objects.select_related('company').all()
class ProductCreateView(CreateView):
  model = Product
  form_class = ProductForm
  template_name = 'crud_app/product_form.html'
  success_url = reverse_lazy('product_list')
  def form_valid(self, form):
    form.instance.image = self.request.FILES.get('image')
    return super().form_valid(form)

class ProductUpdateView(UpdateView):
  model = Product
  form_class = ProductForm
  template_name = 'crud_app/product_form.html'
  success_url = reverse_lazy('product_list')
  def form_valid(self, form):
    form.instance.image = self.request.FILES.get('image')
    return super().form_valid(form)

class ProductDeleteView(DeleteView):
  model = Product
  template_name = 'crud_app/product_confirm_delete.html'
  success_url = reverse_lazy('product_list')