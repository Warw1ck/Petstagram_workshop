from django import forms

from petstagram.common.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'placeholder': 'Add comment...'}),
                   }

class SearchForm(forms.Form):
    pet_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Search for pet name...'})
    )