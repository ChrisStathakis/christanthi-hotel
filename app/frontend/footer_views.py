from django.views.generic import TemplateView
from django.shortcuts import reverse


class TermOfUseView(TemplateView):
    template_name = 'gr/footer_views/term_of_use.html'

    def get_context_data(self, **kwargs):
        context = super(TermOfUseView, self).get_context_data(**kwargs)
        context['page_title'] = 'Όροι χρήσης'
        context['eng_link'] = reverse('term_of_use_gr')
        return context


class PrivacyCookiesView(TemplateView):
    template_name = 'gr/footer_views/politics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Cookies'
        context['eng_link'] = reverse('privacy_eng')
        return context


class TermOfUseEngView(TemplateView):
    template_name = 'eng/footer_views/term_of_use.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = ''
        context['eng_link'] = ''
        return context


class PrivacyCookiesEngView(TemplateView):
    template_name = 'eng/footer_views/politics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Privacy and Cookies'
        context['eng_link'] = reverse('privacy_gr')
        return context
