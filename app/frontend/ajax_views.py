from django.template.loader import render_to_string
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from discover.models import Discover

def show_ajax_modal_gr_view(request, slug):
    print('gr')
    obj = get_object_or_404(Discover, slug=slug)
    data = dict()
    data['result'] = render_to_string(
        template_name='ajax_views/discover_modal_gr.html',
        request=request,
        context={
            'instance': obj
        }
    )
    return JsonResponse(data)


def show_ajax_modal_eng_view(request, slug):
    obj = get_object_or_404(Discover, slug=slug)
    print('backend on action!')
    data = dict()
    data['result'] = render_to_string(
        template_name='ajax_views/discover_modal_eng.html',
        request=request,
        context={
            'instance': obj
        }
    )
    print('back end ready to return data')
    return JsonResponse(data)
