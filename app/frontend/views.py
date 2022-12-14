from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib import messages
from django.http import HttpResponse
from .forms import ContactForm
from .models import Banner, Contact, Instagram
from rooms.models import Room
from discover.models import Discover


class HomepageView(TemplateView):
    template_name = 'gr/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['page_title'] = 'Αρχική Σελίδα'
        context['banners'] = Banner.objects.filter(active=True)
        context['rooms'] = Room.objects.filter(active=True)
        context['eng_link'] = reverse('homepage_eng')
        context['discovers'] = Discover.objects.filter(active=True, is_favorite=True)[:3]
        return context


class AboutUsView(TemplateView):
    template_name = 'gr/aboutus_view.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['page_title'] = 'Ποιοι Είμαστε'
        context['eng_link'] = reverse('about_us_eng')
        context['photos'] = Banner.my_query.get_active().filter()
        return context


class RoomsListView(ListView):
    queryset = Room.objects.filter(active=True)
    model = Room
    template_name = 'gr/room_list_view.html'

    def get_context_data(self,  **kwargs):
        context = super(RoomsListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Τα δωμάτια μας'
        context['eng_link'] = reverse('room_list_eng')

        return context


class RoomDetailView(DetailView):
    queryset = Room.objects.filter(active=True)
    model = Room
    template_name = 'gr/room_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super(RoomDetailView, self).get_context_data(**kwargs)
        context['page_title'] = self.object.title
        # context['keywords'] = ''
        context['eng_link'] = self.object.get_absolute_url_eng
        return context


class DiscoverListView(ListView):
    queryset = Discover.objects.filter(active=True)
    model = Discover
    template_name = 'gr/discover_list_view.html'

    def get_context_data(self,  **kwargs):
        context = super(DiscoverListView, self).get_context_data(**kwargs)
        context['page_title'] = 'Κοντινοί Προορισμοί'
        context['eng_link'] = reverse('discover_list_eng')
        return context


class DiscoverDetailGrView(DetailView):
    queryset = Discover.objects.filter(active=True)
    model = Discover
    template_name = 'gr/discover_detail_view.html'

    def get_context_data(self, **kwargs):
        context = super(DiscoverDetailGrView, self).get_context_data(**kwargs)
        context['page_title'] = self.object.title
        context['eng_link'] = self.object.get_absolute_eng_url()
        return context


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'gr/contact.html'
    success_url = reverse_lazy('contact_gr')

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['eng_link'] = reverse('contact_eng')
        context['page_title'] = 'Επικοινωνία'
        return context

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Η ερώτηση σας καταχωρήθηκε επιτυχώς')
        Contact.send_email(form)
        Contact.inform_admin_email(form)
        return super(ContactView, self).form_valid(form)


def error_404_page(request, exception):
    return render(request, '404_error.html')
    # response.status_code = 404
    # return response


def favicon_img_view(request):
    image_data = open('favicon.ico').read()
    return HttpResponse(image_data, content_type='ico')