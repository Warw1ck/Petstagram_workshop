from django import forms

from petstagram.pets.models import Pet


class BasePetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']

        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Pet name'}),
                   'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
                   'personal_photo': forms.URLInput(attrs={'placeholder': 'Link to image'})}
        labels = {'name': 'Pet name',
                  'date_of_birth': 'Date of birth',
                  'personal_photo': 'Link to image'}


class PetForm(BasePetForm):
    pass


class EditPetForm(BasePetForm):
    pass


class DeletePetForm(BasePetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disable'] = 'disable'
