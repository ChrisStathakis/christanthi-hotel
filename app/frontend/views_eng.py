from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib import messages

from .forms import ContactFormEng
from .models import Banner, Contact
from rooms.models import Room
from discover.models import Discover, DiscoverCategory


class HomepageEngView(TemplateView):
    template_name = 'eng/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageEngView, self).get_context_data(**kwargs)
        context['page_title'] = 'Homepage'
        context['banners'] = Banner.objects.filter(active=True)
        context['rooms'] = Room.objects.filter(active=True)
        context['discovers'] = Discover.objects.filter(active=True, is_favorite=True)[:3]
        context['discovers_2'] = Discover.objects.filter(active=True, is_favorite=True)[3:6]
        context['greek_link'] = reverse('homepage_gr')
        return context


class AboutUsEngView(TemplateView):
    template_name = 'eng/about_us_view.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsEngView, self).get_context_data(**kwargs)
        context['page_title'] = 'About us'
        context['greek_link'] = reverse('about_us_gr')

        return context


class RoomsListEngView(ListView):
    queryset = Room.objects.filter(active=True)
    model = Room
    template_name = 'eng/room_list_view.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Rooms'
        context['greek_link'] = reverse('room_list_gr')
        return context


class RoomDetailEngView(DetailView):
    queryset = Room.objects.filter(active=True)
    model = Room
    template_name = 'eng/room_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.object.title_eng
        context['greek_link'] = self.object.get_absolute_url()
        return context


class DiscoverListEngView(ListView):
    queryset = Discover.objects.filter(active=True)
    model = Discover
    template_name = 'eng/discover_list_view.html'

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = DiscoverCategory.objects.all()
        context['page_title'] = 'Destinations'
        context['greek_link'] = reverse('discover_list_gr')
        return context


class DiscoverDetailEngView(DetailView):
    queryset = Discover.objects.filter(active=True)
    model = Discover
    template_name = 'eng/discover_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super(DiscoverDetailEngView, self).get_context_data(**kwargs)
        context['page_title'] = self.object.title_eng
        context['greek_link'] = self.object.get_absolute_url()
        return context


class ContactEngView(CreateView):
    model = Contact
    form_class = ContactFormEng
    template_name = 'eng/contact.html'
    success_url = reverse_lazy('contact_eng')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'We received your message, and we will try to answer you shortly.')
        Contact.send_email(form, gr=False)
        Contact.inform_admin_email(form)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ContactEngView, self).get_context_data(**kwargs)
        context['greek_link'] = reverse('contact_gr')
        context['page_title'] = 'Contact'
        return context

