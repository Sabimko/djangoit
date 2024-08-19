from django.shortcuts import render

# Create your views here.
def itpark(request):
    context = {
        'title':'it park',
        'description':'it  курсы в Оше',
        'course':'Курсы',
        'bakend':'Бэкенд',
        'front':'Фронтенд',
        'andr':'Андроид'
    }
    return render(request, 'itpark.html', context=context)