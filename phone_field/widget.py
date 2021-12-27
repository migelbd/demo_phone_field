from django import forms


class PhoneInputWidget(forms.TextInput):
    template_name = 'phone_field/widget/phone_widget.html'
    mask = '+7 (999) 999-99-99'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['mask'] = self.mask
        return context

    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.0.min.js',
            'phone_field/js/inputmask/jquery.inputmask.min.js',
            'phone_field/js/inputmask/inputmask.min.js',
            'phone_field/js/inputmask/bindings/inputmask.binding.js',
            'phone_field/js/inputmask/pasteplugin.js'
        )
