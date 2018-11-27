from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime
from .models import BookInstance


# class RenewBookForm(forms.Form):
#     renewal_date = forms.DateField(help_text='Enter a date between now and 4 weeks (default 3)')

#     def clean_renewal_date(self):
#         data = self.cleaned_data['renewal_date']
#         if data < datetime.date.today():
#             print('HERE_1')
#             raise ValidationError(_('Invalid date - renewal in past'))
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             print('HERE_1')
#             raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
#         return data


class RenewBookForm(forms.ModelForm):
    def clean_renewal_date(self):
        data = self.cleaned_data['renewal_date']
        if data < datetime.today():
            raise ValidationError(_('Invalid date - renewal in past'))
        if data > datetime.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
        return data

    class Meta:
        model = BookInstance
        fields = ['due_back',]
        labels = {'due_back': _('Renewal Date'),}
        help_text = {'due_back': _('Enter a date between now and 4 weeks (default 3).'),}
