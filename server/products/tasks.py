import nbs
from django.apps import apps
from celery import shared_task

@shared_task
def scrape_product(url):
  if url is None:
    return None
  elif url == "":
    return
  ProductScrapeEvent = apps.get_model('products', 'ProductScrapeEvent')
  data = nbs.scrape(url)
  ProductScrapeEvent.objects.create_scrape_event(data, url=url)
  return data


# next step in to set this as a periodic task in the django admin periodic panel.
@shared_task
def scrape_product_daily():
  product = apps.get_model('products', 'Product')
  qs = product.objects.filet(active=True)
  for obj in qs:
    url = obj.url
    scrape_product.delay(url)