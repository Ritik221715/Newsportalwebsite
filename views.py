from django.shortcuts import render

from django.http import HttpResponse
from django.db.models import Q
from .models import *


def index(request):
    data=category.objects.all().order_by('-id')[0:18]
    data1=slider.objects.all().order_by('-id')[0:3]
    data2=tbl_city.objects.all().order_by('-id')[0:24]
    data3=tbl_news.objects.all().order_by('-id')[0:12]
    data4=tbl_news.objects.all().order_by('-id')[0:10]
    md={'cdata':data,'sdata':data1,'citydata':data2,'tdata':data3,'lndata':data4}
    return render(request,'index.html',md)
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        message=request.POST.get('msg')
        contactus(Name=name,Email=email,Mobile=mobile,Message=message).save()
        return HttpResponse("<script>alert('Thank you for contact with us');location.href=('/contact/')</script>")
    return render(request,'contact.html')
def faqs(request):
    return render(request,'faqs.html')
def jobs(request):
    data=tbl_jobs.objects.all().order_by('-id')
    jd={'jdata':data}
    return render(request,'jobs.html',jd)
def login(request):
    return render(request,'login.html')

def news(request):
        catid = request.GET.get('catid')
        cityid = request.GET.get('cityid')
        searchdata = request.GET.get('search')
        data = ""
        if catid is not None:
            data = tbl_news.objects.all().filter(news_category=catid)
        elif cityid is not None:
            data = tbl_news.objects.all().filter(news_city=cityid)
        elif searchdata is not None:
            data = tbl_news.objects.all().filter(
                Q(headline__icontains=searchdata) | Q(news_description__icontains=searchdata) | Q(
                    news_city__city_name__icontains=searchdata) | Q(news_category__category_name__icontains=searchdata))
        else:
            data = tbl_news.objects.all().order_by('-id')
        citydata = tbl_city.objects.all().order_by('-id')
        categorydata = category.objects.all().order_by('-id')
        nd = {'ndata': data, 'citydata': citydata, 'categorydata': categorydata}
        return render(request, 'news.html', nd)
def videos(request):
    data=video_news.objects.all().order_by('-id')
    mydict={"vdata":data}
    return render(request,'videos.html',mydict)
def newsdetails(request):
    x=request.GET.get('nid')
    data=tbl_news.objects.all().filter(id=x)
    mydict={'ndata':data}
    return render(request,'newsdetails.html',mydict)
def sliderdetails(request):
    a=request.GET.get('sid')
    data=slider.objects.all().filter(id=a)
    mydict={'sldata':data}
    return render(request,'sliderdetails.html',mydict)
def categorydetails(request):
    a=request.GET.get('catid')
    data=tbl_news.objects.all().filter(id=a)
    if a is not None:
        data = tbl_news.objects.all().filter(news_category=a)
    else:
        data = tbl_news.objects.all().order_by('-id')
    mydict={'catdata':data}
    return render(request,'categorydetils.html',mydict)
def profile(request):
    return render(request,'myprofile.html')
# Create your views here.
