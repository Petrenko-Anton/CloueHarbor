
from django.forms import ModelForm, CharField, TextInput, EmailField, EmailInput, DateField, DateInput, SelectDateWidget
from django import forms
from .models import Contact
from datetime import date

MONTHS = {
    1: "січня",
    2: "лютий",
    3: "березень",
    4: "квітень",
    5: "травень",
    6: "червень",
    7: "липень",
    8: "серпень",
    9: "вересень",
    10: "жовтень",
    11: "листопад",
    12: "грудень",
}


class ContactForm(ModelForm):

    first_name = CharField(max_length=100, widget=TextInput(
        attrs={'class': "form-control"}))
    last_name = CharField(max_length=100, widget=TextInput(
        attrs={'class': "form-control"}))
    email = EmailField(max_length=100, required=True,
                       widget=EmailInput(attrs={'class': "form-control"}))
    phone = CharField(max_length=100, widget=TextInput(
        attrs={'class': "form-control"}))
    # birth_date = DateField(required=True, widget=DateInput(
    #     attrs={'class': "form-control"}))
    birth_date = DateField(
        required=True, widget=SelectDateWidget(months=MONTHS, years=[x for x in range(date.today().year - 100, date.today().year + 1)]))

########################################################################################
#    comment = CharField(max_length=100, widget=TextInput(attrs={'class': "form-control"}))
# it was commented becasue html does not correspond to this form that is why it does not work if not commented

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'phone', 'birth_date')


class SearchContactNameForm(forms.Form):
    search_name = forms.CharField(label="search_name", max_length=100)


class SearchContactEmailForm(forms.Form):
    search_email = forms.EmailField(max_length=100, required=True,
                                    widget=EmailInput(attrs={'class': "form-control"}))
