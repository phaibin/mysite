from django.shortcuts import render_to_response
from django.http import HttpResponse
from books.models import Book
    
def search(request):
    errors = []
    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            errors.append('Enter a search term.')
        elif len(query) > 20:
            errors.append('Please enter a most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=query)
            return render_to_response('books/search_results.html',
            locals())
    return render_to_response('books/search_form.html', {'errors': errors})