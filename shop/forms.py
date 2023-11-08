from django import forms
from .models import Order, Contact


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("name", "email", "phone", "address")


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "phone", "message")
