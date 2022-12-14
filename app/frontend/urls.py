from django.urls import path
from django.conf.urls import url
from django.contrib.sitemaps.views import sitemap
from .views import HomepageView, RoomsListView, RoomDetailView, DiscoverListView, ContactView, AboutUsView, DiscoverDetailGrView
from .views_eng import HomepageEngView, RoomsListEngView, RoomDetailEngView, DiscoverListEngView, ContactEngView, AboutUsEngView, DiscoverDetailEngView
from .footer_views import TermOfUseView, TermOfUseEngView, PrivacyCookiesEngView, PrivacyCookiesView
from .ajax_views import show_ajax_modal_gr_view, show_ajax_modal_eng_view

from .sitemaps import StaticViewsSitemap
from rooms.sitemap import RoomSitemap
from discover.sitemap import DiscoverCategorySitemap


sitemaps = {
    'static': StaticViewsSitemap,
    'rooms': RoomSitemap,

}

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage_gr'),
    path('διαμονη/', RoomsListView.as_view(), name='room_list_gr'),
    path('η-ιστορια-μας/', AboutUsView.as_view(), name='about_us_gr'),
    path('τα-δωματια-μας/δωματιο/<slug:slug>/', RoomDetailView.as_view(), name='room_detail_gr'),
    path('προορισμοί/', DiscoverListView.as_view(), name='discover_list_gr'),
    url(r'^προορισμός/(?P<slug>[-\w]+)/$',  DiscoverDetailGrView.as_view(), name='discover_detail_view'),
    path('επικοινωνια/', ContactView.as_view(), name='contact_gr'),
    path('όροι-χρήσης/', TermOfUseView.as_view(), name='term_of_use_gr'),
    path('προσωπικά-δεδομένα-cookies/', PrivacyCookiesView.as_view(), name='privacy_gr'),


    path('eng/', HomepageEngView.as_view(), name='homepage_eng'),
    path('eng/our-story/', AboutUsEngView.as_view(), name='about_us_eng'),
    path('eng/rooms/', RoomsListEngView.as_view(), name='room_list_eng'),
    path('eng/rooms/room/<slug:slug>/', RoomDetailEngView.as_view(), name='room_detail_eng'),
    path('eng/discover/', DiscoverListEngView.as_view(), name='discover_list_eng'),
    url(r'^eng/discover/details/(?P<slug>[-\w]+)/$', DiscoverDetailEngView.as_view(), name='discover_detail_eng'),
    path('eng/contact/', ContactEngView.as_view(), name='contact_eng'),

    path('eng/term-of-use/', TermOfUseEngView.as_view(), name='term_of_use_eng'),
    path('eng/personal-data/', PrivacyCookiesEngView.as_view(), name='privacy_eng'),

    # ajax views
    url(r'ajax/show-modal-discover/(?P<slug>[-\w]+)/$', show_ajax_modal_gr_view, name='show_discover_modal_gr'),
    url(r'eng/ajax/show-discover/(?P<slug>[-\w]+)/$', show_ajax_modal_eng_view, name='show_discover_modal_eng'),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),



]

