from django.forms import ModelForm
from .models import Review, Store

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'review', 'rating']

class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'address', 'phone']