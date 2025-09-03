from django.shortcuts import render


def show_main(request):
    context = {
        'npm' : '2406420702',
        'name': 'Heraldo Arman',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)