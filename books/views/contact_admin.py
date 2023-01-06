from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from django.conf import settings
from django.views.generic.edit import FormView

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from PIL import Image

class ContactForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        # call original initializator
        super().__init__(*args, **kwargs)
        # this helper object allows us to customize form
        self.helper = FormHelper(self)
        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')
        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 col-form-label'
        self.helper.field_class = 'col-sm-10'
        # form buttons
        self.helper.add_input(Submit('send_button', 'Надіслати'))

    from_email = forms.EmailField(label="Ваша Емейл Адреса")
    subject = forms.CharField(label="Заголовок листа", max_length=128)
    message = forms.CharField(label="Текст повідомлення",max_length=2560,
                              widget=forms.Textarea)

class ContactAdminView(FormView):
    form_class = ContactForm
    template_name = 'contact_admin/form.html'

    def form_valid(self, form):
        from_email = form.cleaned_data.get('from_email')
        subject = form.cleaned_data.get('subject')
        message = form.cleaned_data.get('message')
        try:
            send_mail(subject, message, from_email, [settings.ADMIN_EMAIL])
        except Exception:
            message = 'Під час відправки листа виникла непередбачувана помилка. Спробуйте скористатись даною формою пізніше.'
        else:
            message = 'Повідомлення успішно надіслане!'
        return HttpResponseRedirect(self.get_success_url() + f'?status_message={message}')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_success_url(self):
        return reverse('contact_admin')