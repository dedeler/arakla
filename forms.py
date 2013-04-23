from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext_lazy, string_concat
from askbot.forms import AskForm, AnswerForm

class TitleField(forms.CharField):
    """Field receiving question title"""
    def __init__(self, *args, **kwargs):
        super(TitleField, self).__init__(*args, **kwargs)
        self.required = kwargs.get('required', True)
        self.widget = forms.TextInput(
                            attrs={'size': 70, 'autocomplete': 'off'}
                        )
        self.max_length = 255
        self.label = _('title')
        self.help_text = _(
            'Please enter your question'
        )
        self.initial = ''

class GistForm(AskForm):
    gist_id = forms.CharField(max_length=100)

class GanswerForm(AnswerForm):
    def __init__(self, *args, **kwargs):
        super(GanswerForm, self).__init__(*args, **kwargs)
        print('initialized my ganswer')
	