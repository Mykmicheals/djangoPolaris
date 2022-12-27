from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()


class AddressForm(forms.Form):
    address_1 = forms.CharField()
    city = forms.CharField()
    zip_code = forms.CharField()


class BankAccount(forms.Form):
    account_number = forms.CharField()
 