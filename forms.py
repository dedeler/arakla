from django import forms
from askbot.forms import AskForm 

class GistForm(AskForm):
    gist_id = forms.CharField(max_length=100)
    print('created gist form')