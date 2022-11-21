from django.urls import reverse

from newsletter.forms import NewsLetterForm, NewsLetterFormEng


def frontend_site_data(request):

    return {
        'page_keywords': 'Μονεμβασια, ξενοδοχείο, δωμάτια, χαλάρώση, κάστρο, διαμερίσματα, Gregory Hotel',
        'page_description': "Ανακαλύψτε τη μαγεία της Μονεμβασιάς με αφετηρία σας το  Gregory's house!",
        'page_keywords_eng': 'Monemvasia, hotel, rooms, castle, apartments, Gregory Hotel',
        'page_description_eng': "Choose Gregory's house as your starting point to discover the magnificent",
        'eng_link': reverse('homepage_eng'),
        'greek_link': reverse('homepage_eng'),
        'newsletterFormGr': NewsLetterForm(),
        'newsletterFormEng': NewsLetterFormEng(),
    }