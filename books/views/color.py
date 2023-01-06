from django.shortcuts import render

from books.models import Books

def color_view(request):
    if request.method == 'POST':
        bookmark = request.POST.get('bookmark')
        captal = request.POST.get('captal')
        color_model = Books(bookmark=bookmark, captal=captal)
        color_model.save()
    return render(request, 'books_list.html', {'color_model': color_model})
