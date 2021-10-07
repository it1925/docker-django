from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.template import engines

django_engine = engines['django']
template = django_engine.from_string("Hello {{ name }}!")

def index(request):
    a = HttpResponse("Hello, world. You're at the polls index.")
    return a
def test(request):
    template = get_template('test.html')
    return HttpResponse(template.render(request))
