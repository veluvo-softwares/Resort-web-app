from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='LukenyaGetawayHomepage'),
    path('about-us', views.aboutus, name='LukenyaGetawayInfo'),
    path('contact-us', views.contacts, name='ContactLukenyaGetaway'),
    path('news', views.news, name='LukenyaGetawayNews'),
    # path('newslet', views.newslet, name='newsletter'),
    path('rooms', views.rooms, name='LukenyaGetawayRooms'),
    path('amenities', views.amenities, name='LukenyaGetawayAmenities'),
    path('activities', views.activities, name='LukenyaGetawayActivities'),
    # path('virtualtour', views.logout, name="virtual tour"),
    path('reservations', views.reservations, name="LukenyaGetawayReservations"),
    path('gallery', views.Gallery, name="LukenyaGetawayGallery"),
    
]