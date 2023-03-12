from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Comment


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounder-0'


class CommentForm(forms.ModelForm):
    """ Class for adding a comment to a post """
    class Meta:
        """ Meta class """
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control', 'rows': 3
            })
        }


class RatingForm(forms.Form):
    rating = forms.DecimalField(max_digits=3, decimal_places=1)

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if not (0 <= rating <= 5):
            raise forms.ValidationError('Rating must be between 0 and 5.')
        return rating
