from django.shortcuts import render, get_object_or_404, redirect
from .models import Company, Product
from .forms import CompanyForm, ProductForm


# หน้าแรก
def home(request):
  return render(request, 'crud_app/home.html')


# แสดงรายชื่อบริษัท
def company_list(request):
  companies = Company.objects.all()
  return render(request, 'crud_app/company_list.html', {'companies': companies})


# แสดงฟอร์มเพิ่มข้อมูลบริษัท
def company_create(request):
  if request.method == 'POST':
    form = CompanyForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('company_list')
    else:
      return render(request, 'crud_app/company_form.html', {'form': form, 'errors': form.errors})
  else:
    form = CompanyForm()
  return render(request, 'crud_app/company_form.html', {'form': form})


# แสดงฟอร์มแก้ไขข้อมูลบริษัท
def company_update(request, pk):
  company = get_object_or_404(Company, pk=pk)
  if request.method == 'POST':
    form = CompanyForm(request.POST, instance=company)
    if form.is_valid():
      form.save()
      return redirect('company_list')
    else:
      return render(request, 'crud_app/company_form.html', {'form': form, 'errors': form.errors})
  else:
    form = CompanyForm(instance=company)
  return render(request, 'crud_app/company_form.html', {'form': form})


# แสดงหน้าลบข้อมูลบริษัท
def company_delete(request, pk):
  company = get_object_or_404(Company, pk=pk)
  if request.method == 'POST':
    company.delete()
    return redirect('company_list')
  return render(request, 'crud_app/company_confirm_delete.html', {'company': company})


# แสดงรายชื่อสินค้า
def product_list(request):
  products = Product.objects.select_related('company').all()
  return render(request, 'crud_app/product_list.html', {'products': products})


# แสดงฟอร์มเพิ่มข้อมูลสินค้า
def product_create(request):
  if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('product_list')
    else:
      return render(request, 'crud_app/product_form.html', {'form': form, 'errors': form.errors})
  else:
    form = ProductForm()
  return render(request, 'crud_app/product_form.html', {'form': form})


# แสดงฟอร์มแก้ไขข้อมูลสินค้า
def product_update(request, pk):
  product = get_object_or_404(Product, pk=pk)
  if request.method == 'POST':
    form = ProductForm(request.POST, request.FILES, instance=product)
    if form.is_valid():
      form.save()
      return redirect('product_list')
    else:
      return render(request, 'crud_app/product_form.html', {'form': form, 'errors': form.errors})
  else:
    form = ProductForm(instance=product)
  return render(request, 'crud_app/product_form.html', {'form': form})


# แสดงหน้าลบข้อมูลสินค้า
def product_delete(request, pk):
  product = get_object_or_404(Product, pk=pk)
  if request.method == 'POST':
    product.delete()
    return redirect('product_list')
  return render(request, 'crud_app/product_confirm_delete.html', {'product': product})