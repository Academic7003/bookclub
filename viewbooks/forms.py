from django.forms import ModelForm
from viewbooks.models import *


class BuyerForm(ModelForm):

    class Meta:
        model = BuyModel
        fields = '__all__'