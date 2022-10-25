# from django.contrib import messages
from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from .models import Rooms, Testimonials, News, category, Gallery
# from .ContactForm import ContactForm
from django.core.paginator import Paginator, Page, PageNotAnInteger, EmptyPage


# Create your views here.
def index(request):
    room = Rooms.objects.all()
    test = Testimonials.objects.all()
    # nws_latest = news.objects.all().order_by('-news_date')[:3]

    # return render(request, "index.html", {'dests': dests, 'testimon': testimon, 'nws_latest': nws_latest})
    return render(request, "index.html", {'room': room, 'test': test})


def aboutus(request):
    
    return render(request, "about-us.html")

def rooms(request):
    
    return render(request, "rooms.html")

def main(request):
    
    return render(request, "main.html")

def reservations(request):
    
    return render(request, "check-availability.html")

def contacts(request):
    
    return render(request, "contact.html")


def news(request):
    
    return render(request, "news.html")

# def gallery(request):
#     img_cat = image_category.objects.all()
#     images = Gallery.objects.all()
#     return render(request, "gallery.html", {"img_cat": img_cat,"images":images})


def gallery(request):
    return render(request, "gallery.html")

def activities(request):
    
    return render(request, "activities.html")

def amenities(request):
    
    return render(request, "amenities.html")

# def contacts(request):
#     form = ContactForm

#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             cont_name = request.POST['Name']
#             cont_email = request.POST['Email']
#             cont_subject = request.POST['Subject']
#             cont_msg = request.POST['Message']
#             conts = contact(Name=cont_name, Email=cont_email, Subject=cont_subject, Message=cont_msg)
#             conts.save()
#             return redirect('/')
#         else:
#             messages.info(request, 'Forms Went Wrong')
#             return HttpResponseRedirect(request.path_info)

#     else:
#         return render(request, "contact.html", {'form': form})


def news(request):
    latest_news = News.objects.all().order_by('-news_date')[:5]
    cat = category.objects.all()
    news_set = News.objects.all()
    # pagination below
    paginator = Paginator(news_set, 5)
    Page = request.GET.get('page')
    try:
        nws = paginator.page(Page)
    except PageNotAnInteger:
        nws = paginator.page(1)
    except EmptyPage:
        nws = paginator.page(paginator.num_pages)

    return render(request, "news.html", {'nws': nws, 'cat': cat, 'latest_news': latest_news})




# def newsletter(request):
#     if request.method == 'POST':
#         nl_name = request.POST['nl_name']
#         nl_email = request.POST['nl_email']
#         newsl = newsletter(nl_name=nl_name, nl_email=nl_email)
#         newsl.save()
#         return redirect('/')

