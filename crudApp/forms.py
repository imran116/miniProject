from django import forms

from crudApp.models import Artist


class ArtistForm(forms.ModelForm):
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={
        'type':'date'
    }))



    class Meta:
        model = Artist
        # exclude = ['date_of_birth']
        fields = '__all__'

