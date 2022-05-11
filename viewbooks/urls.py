from django.urls import path
from viewbooks.views import *

app_name = 'books'


urlpatterns = [
    path('uzb', UzBooksView.as_view(), name='uzb'),
    path('rus', RusBooksView.as_view(), name='rus'),
    path('eng', EngBooksView.as_view(), name='eng'),
    path('uzdetail/<int:pk>', UzBooksDetailView.as_view(), name='uzdetail'),
    path('rusdetail/<int:pk>', RusBooksDetailView.as_view(), name='rusdetail'),
    path('engdetail/<int:pk>', EngBooksDetailView.as_view(), name='engdetail'),
    path('uzbbuy', uzbbuy, name='uzbbuy'),
    path('rusbuy', rusbuy, name='rusbuy'),
    path('engbuy', engbuy, name='engbuy'),
    path('onas', Onas.as_view(), name='onas'),

]
