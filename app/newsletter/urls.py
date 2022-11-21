from django.urls import path


from .views import form_valid_newsletter_form_view, form_valid_newsletter_form_view_eng, newsletter_page_view


app_name = 'newsletter'

urlpatterns = [
    path('newsletter/validate-form/', form_valid_newsletter_form_view, name='newsletter_valid_form'),
    path('eng/newsletter/validate-form/', form_valid_newsletter_form_view_eng, name='newsletter_valid_form_eng'),
    path('newsletter/<slug:slug>/', newsletter_page_view, name='newsletter_page_view'),

]