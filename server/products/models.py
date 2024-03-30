from django.db import models
from .tasks import scrape_product

class Product(models.Model):
  product_title = models.CharField(max_length=100, unique=True, db_index=True)
  product_price = models.FloatField(blank=True, null=True, default=0.0)
  url = models.URLField(blank=True, null=True)
  active = models.BooleanField(default=True, help_text="Scrape Daily?")
  # trigger_scrape = models.BooleanField(default=False)
  # _trigger_scrape = models.BooleanField(default=False)
  
  # def save(self, *args, **kwargs):
  #   if self.url and self.pk:
  #     if self.trigger_scrape is not self._trigger_scrape:
  #       self.trigger_scrape = False
  #       self._trigger_scrape = False
  #       scrape_product.delay(self.url)
  #   super().save(*args, **kwargs)
  
class ProductScrapeEventManager(models.Manager):
  def create_scrape_event(self, data, url=None):
    product_title = data.get('product_title') or None
    if product_title is None:
      return None
    product, _ = Product.objects.update_or_create(
      product_title=product_title,
      defaults={
        "product_title": data.get("product_title") or "",
        "prouct_price": data.get("product_price") or 0.0,
        "url": url,
      }
    )
    event = self.create(
      product=product,
      product_title=product_title
    )
    return event

class ProductScrapeEvent(models.Model):
  product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='scrape_events')
  product_title = models.CharField(max_length=100, blank=True, null=True)
  product_price = models.FloatField(blank=True, null=True, default=0.0)
  url = models.URLField(blank=True, null=True)
  
  objects = ProductScrapeEventManager()