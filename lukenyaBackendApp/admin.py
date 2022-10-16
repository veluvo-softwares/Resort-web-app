from django.contrib import admin
from .models import Rooms,Testimonials,News,category


# Register your models here.


class RoomsA(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'desc', 'kes_price', 'usd_price')


class TestimonialsA(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'customer_testimonial', 'customer_designation')


# class aboutA(admin.ModelAdmin):
#     list_display = ('abt_name', 'abt_desc', 'abt_img')


# class about_cardA(admin.ModelAdmin):
#     list_display = ('abt_card_name', 'abt_card_desc', 'abt_card_img')


# class about_teamA(admin.ModelAdmin):
#     list_display = ('abt_team_name', 'abt_team_desc', 'abt_team_img')


class newsA(admin.ModelAdmin):
    list_display = ('news_header', 'news_description', 'news_img', 'news_date')


class categoryA(admin.ModelAdmin):
    list_display = ('cat_name', 'cat_desc')


# class newsletterA(admin.ModelAdmin):
#     list_display = ('nl_name', 'nl_email')


# class contactA(admin.ModelAdmin):
#     list_display = ('Name', 'Email', 'Subject')


admin.site.register(Rooms, RoomsA)
admin.site.register(Testimonials, TestimonialsA)
# admin.site.register(about, aboutA)
# admin.site.register(about_card, about_cardA)
# admin.site.register(about_team, about_teamA)
admin.site.register(News, newsA)
admin.site.register(category, categoryA)
# admin.site.register(newsletter, newsletterA)
# admin.site.register(contact, contactA)

