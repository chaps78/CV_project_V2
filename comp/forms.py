from django import forms


class ContactForm(forms.Form):
    nom = forms.CharField(
        label='Nom',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
        )

    prenom = forms.CharField(
        label='Prenom',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True
        )

    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        required=True)
#    nom = forms.CharField(max_length=10)
    pass


