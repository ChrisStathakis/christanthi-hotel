from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib import messages
# Create your views here.

from .forms import NewsLetterForm
from .models import NewsLetterPage


def form_valid_newsletter_form_view(request):
    form = NewsLetterForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        messages.success(request, f'Το {obj.email} καταχωρήθηκε. Ευχαριστούμε!')
    else:
        messages.success(request, f'Το email που χρησιμοποιείται υπάρχει ήδη στην λίστα μας. Ευχαριστούμε!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def form_valid_newsletter_form_view_eng(request):
    form = NewsLetterForm(request.POST or None)
    if form.is_valid():
        obj = form.save()
        messages.success(request, f'{obj.email} is added to our list. Thank You!')
    else:
        messages.success(request, f'The email which used is already added to our list. Thank You!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def newsletter_page_view(request, slug):
    obj = get_object_or_404(NewsLetterPage, slug=slug)
    if not obj.active:
        return HttpResponseRedirect('/')
    form = NewsLetterForm()
    return render(request, 'newsletter/page.html', context={'obj': obj, 'form': form})
