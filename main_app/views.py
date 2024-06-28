from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, UpdateView
from .models import Book, Review, Store
from .forms import ReviewForm, StoreForm


# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})

def about(request):
    return render(request, 'books/about.html')

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    reviews = book.review_set.all()
    stores = book.store.all()
    excluded = Store.objects.exclude(id__in=stores)
    print(excluded)
    return render(request, 'books/detail.html', {'book': book, 'reviews': reviews, 'stores': stores, 'e_stores': excluded})

def add_review(request, book_id):
    book = Book.objects.get(id=book_id)
    name = request.POST.get("name")
    review = request.POST.get("review")
    rating = request.POST.get("rating")
    review = Review.objects.create(name=name, review=review, rating=rating, book=book)
    review.save()
    return redirect('/')

def store_create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        return render(request, 'books/add.html', {'store_form': StoreForm()})
    
def store_list(request):
    store = Store.objects.all()
    return render(request, 'books/slist.html', {'stores': store})

def assoc_store(request, store_id, book_id):
    book = Book.objects.get(id=book_id)
    store = Store.objects.get(id=store_id)
    book.store.add(store)
    return redirect('detail' , book_id=book_id)

class CreateBook(CreateView):
    model = Book
    fields = '__all__'

class UpdateBook(UpdateView):
    model = Book
    fields = ['author', 'isbn', 'published']

class DeleteBook(DeleteView):
    model = Book
    success_url = '/'

