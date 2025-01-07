from django.db import models
class Company(models.Model):
  name = models.CharField(max_length=100, unique=True)
  address = models.TextField()

  def __str__(self):
    return self.name

class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='products')
  image = models.ImageField(upload_to='product_images/', null=True, blank=True)
  
  def __str__(self):
    return self.name