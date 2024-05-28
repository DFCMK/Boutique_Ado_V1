from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        friends = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in ccategories] 

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            firld.widget.attrs['class'] = 'border-black rounded-0'



