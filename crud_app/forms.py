from django import forms
from .models import Company, Product

class CompanyForm(forms.ModelForm):
  class Meta:
    model = Company
    fields = ['name', 'address']
    labels = {
    'name': 'ชื่อบริษัท',
    'address': 'ที่อยู่บริษัท'
    }

  def clean_name(self):
    name = self.cleaned_data.get('name')
    if Company.objects.filter(name__iexact=name).exclude(pk=self.instance.pk).exists():
      raise forms.ValidationError("ชื่อบริษัทซ ้ากับข้อมูลในฐานข้อมูล")
    return name

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ['name', 'price', 'company', 'image'] # เพิ่มฟิลด์ image
    labels = {
      'name': 'ชื่อสินค้า',
      'price': 'ราคา',
      'company': 'บริษัท',
      'image': 'รูปสินค้า'
    }

  def clean_price(self):
    price = self.cleaned_data.get('price')
    if price <= 0:
      raise forms.ValidationError("ราคาต้องมากกว่า 0")
    return price

  def clean_image(self):
    image = self.cleaned_data.get('image')
    max_size = 6 * 1024 * 1024 # max upload file size = 6 MB
    if image and image.size > max_size:
      raise forms.ValidationError(f"ไฟล์รูปใหญ่เกิน ( > {max_size / (1024 * 1024)} MB )")
    return image