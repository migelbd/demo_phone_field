from django import forms

from phone_field.widget import PhoneInputWidget


class PhoneField(forms.CharField):
    widget = PhoneInputWidget()

    def to_python(self, value):
        value = super().to_python(value)
        return ''.join([c for c in value if c.isdigit()])
