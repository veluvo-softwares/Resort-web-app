from django.db import models

# # # Create your models here.

class Rooms(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='lukenyaGetawayRooms')
    desc = models.TextField()
    kes_price = models.IntegerField()
    usd_price = models.IntegerField()
    class Meta: 
        verbose_name = "room"
        verbose_name_plural = "rooms"


class Testimonials(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_testimonial = models.TextField()
    customer_designation = models.CharField(default="Customer", max_length=200)
    class Meta: 
        verbose_name = "testimonial"
        verbose_name_plural = "testimonials"

# News model
class News(models.Model):
    news_header = models.CharField(max_length=100)
    news_description = models.TextField()
    news_img = models.ImageField(upload_to='lukenyaGetawayNews')
    news_date = models.DateField()
    class Meta: 
        verbose_name = "news"
        verbose_name_plural = "news"

# Category
class category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_desc = models.TextField()
    class Meta: 
        verbose_name = "category"
        verbose_name_plural = "categories"


# Image Category
class image_category(models.Model):
    category_name = models.CharField(max_length=100)
    category_desc = models.TextField()

    def __str__(self):
        return self.category_name

    # Unique ID for each category
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    # Image name for each category
    class Meta: 
        verbose_name = "image category"
        verbose_name_plural = "image categories"




class Gallery(models.Model):
    image_name = models.CharField(max_length=100)
    image_desc = models.TextField()
    image_url = models.ImageField(upload_to='lukenyaGallery')
    altText = models.TextField(null=True, blank=True)


    # Category of the image
    image_category = models.ForeignKey(image_category, null=True, blank=True, on_delete=models.CASCADE)
    # Change the name of the category in the admin panel
    class Meta: 
        verbose_name = "gallery"
        verbose_name_plural = "galleries"



