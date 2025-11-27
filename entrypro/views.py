from django.http import HttpResponse

def hello_world(request):
    return HttpResponse('<h2>hello ザ　わーるど！</h2>')