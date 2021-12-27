from django.db import models
from phone_field import forms, widget


class PhoneField(models.CharField):

    def __init__(self, *args, **kwargs):
        kwargs.update({
            'max_length': kwargs.get('max_length', 128)
        })
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        value = super().to_python(value)
        return ''.join([c for c in value if c.isdigit()])

    def formfield(self, **kwargs):
        return super().formfield(form_class=forms.PhoneField, **{
            **kwargs,
            'widget': widget.PhoneInputWidget()
        })

    def get_internal_type(self):
        return 'PhoneField'
