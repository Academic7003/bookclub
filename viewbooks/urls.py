from django.urls import path
from viewbooks.views import *

app_name = 'books'


urlpatterns = [
    path('', UzBooksView.as_view(), name='uzb'),
    path('rus', RusBooksView.as_view(), name='rus'),
    path('eng', EngBooksView.as_view(), name='eng'),
    path('uzdetail/<int:pk>', uzbbuy, name='uzdetail'),
    path('rusdetail/<int:pk>', rusbuy, name='rusdetail'),
    path('engdetail/<int:pk>', engbuy, name='engdetail'),
    path('onas', Onas.as_view(), name='onas'),
    path('search/', search_uz, name = 'search')

]
