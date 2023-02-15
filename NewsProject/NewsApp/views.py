from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'NewsApp/news.html');


def indianews(request):
    dict1={'mainmsg':'India News App',
           'submsg1': '100+crores vaccinations done successfully',
           'submsg2':'India is super power in the world ',
           'submsg3':'Agni 5 long range missile (20,000kms) successfully tested',
           'photo':'images/image1.jpg'};
    return render(request,'NewsApp/news.html',context=dict1);


def sportsnews(request):
    dict1={'mainmsg':'Sports News App',
           'submsg1':'India Won womens worldcup 2023',
           'submsg2':'congractulations team india womens for winning worldcup',
           'submsg3':'Im proud to be indian',
           'photo':'images/image2.jpg'};
    return render(request,'NewsApp/news.html',context=dict1);



def technews(request):
    dict1 = {'mainmsg': 'Technology News Page',
             'submsg1': 'Apple to release Apple-14 in 4-models(mini,basic,pro,pro-max',
             'submsg2': 'India starts Semi-conductor chips to World Smartphones',
             'submsg3': 'Tech-jobs more in India than elsewhere in the world',
             'photo': 'images/image3.jpg'};
    return render(request, 'NewsApp/news.html', context=dict1);


