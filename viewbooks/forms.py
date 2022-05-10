from django.forms import ModelForm
from viewbooks.models import *


class UzBuyerForm(ModelForm):

    class Meta:
        model = UzBuyModel
        fields = '__all__'

class RusBuyerForm(ModelForm):

    class Meta:
        model = RusBuyModel
        fields = '__all__'

class EngBuyerForm(ModelForm):

    class Meta:
        model = EngBuyModel
        fields = '__all__'