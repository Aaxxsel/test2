from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from menu_site.models import Test, Question


def index(request):
    context = {'title': 'Главная страница'}
    return render(request, 'menu_site/index.html', context)


def show_tests(request):
    tests = Test.objects.all()
    context = {
        'title': 'Список Тестов',
        'tests': tests,
               }
    return render(request, 'menu_site/tests_list.html', context)


def test_detail(request, slug):
    test = get_object_or_404(Test, slug=slug)
    questions = test.questions.all()
    context = {
        'test': test,
        'questions': questions
    }
    return render(request, 'menu_site/test_detail.html', context)
