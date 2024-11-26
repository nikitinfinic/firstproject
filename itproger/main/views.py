from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Тут', 'Все самое', 'Интерсное'],
        'value': 'Тут все самое Интерсное',
        'Nikita': {
            'car': 'Nope',
            'age': 21,
            'hobby': 'Football'
        }
        }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


